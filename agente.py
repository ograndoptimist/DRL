from simulador import AdmiravelMundoNovo
import numpy as np
from keras import Input
from keras.models import Model
from keras.layers import concatenate, Embedding, Dense, LSTM
from keras.preprocessing.sequence import pad_sequences
from utilidades import preprocessamento, tokenizacao, palavraParaIndice, vetorizacao



class DeepQLearningAgente(object):
    """
        Implementação de um Agente Artificial utilizando-se de Reinforcement Learning e Deep Learning.
        É utilizado o algoritmo off-policy Q-Learning para treinar uma Rede Neural baseada em LSTM.
    """
    def __init__(self):
        with open('vocabulario.txt', 'r') as arquivo:
            vocabulario = arquivo.read()
            vocabulario = ''.join(vocabulario)
            vocabulario = vocabulario.split()
            self.dicionario_de_tokens = palavraParaIndice(vocabulario)
                        
        self.modelo = self.cria_modelo()

    def cria_modelo(self, dimensoes_embedding = 32, dimensoes_lstm = 32, numero_maximo_palavras = 269):
        """
            Implementa a rede neural que escolhe a ação a ser realizada no corrente estado.
        """
        estado = Input(batch_shape = (None, None), name = 'estado')
        acao = Input(batch_shape = (None, None), name = 'acao')

        embedding_compartilhada = Embedding(numero_maximo_palavras, dimensoes_embedding)

        embedding_estado = embedding_compartilhada(estado)
        embedding_acao = embedding_compartilhada(acao)

        lstm_compartilhada = LSTM(dimensoes_lstm)

        lstm_estado = lstm_compartilhada(embedding_estado)
        lstm_acao = lstm_compartilhada(embedding_acao)

        fusao = concatenate([lstm_estado, lstm_acao], axis = -1)
        
        output = Dense(1, activation = 'tanh')(fusao)

        modelo = Model([estado, acao], output)

        modelo.compile(optimizer = 'rmsprop', loss = 'mse', metrics = ['acc'])

        return modelo           

    def transforma(self, texto):
        """
            Realiza a conversão dos textos que descrevem os estados e as ações em vetor de inteiros.
        """
        if isinstance(texto, list):
            vetor = []
            for parte in texto:
                parte = preprocessamento(parte)
                tokens = tokenizacao(parte)
                vetor_aux = vetorizacao(tokens, self.dicionario_de_tokens)
                vetor.append(vetor_aux)
            return vetor                

        texto = preprocessamento(texto)
        tokens = tokenizacao(texto)
        vetor = vetorizacao(tokens, self.dicionario_de_tokens)    

        return vetor

    def q_value(self, estado, acao, epsilon):
        """
            Alimenta o modelo com um estado e uma ação, de forma a obter na saída o Q(s, a).
                ::estado:
                ::acao:
        """
        return self.model.predict([estado, acao])        

    def acao(self, estado, acoes, epsilon, espaco_acoes):
        """
            Seletor de ações.
            ::estado:
            ::acoes:
            ::epsilon:
                Probabilidade de escolher uma ação aleatória.
        """
    
        if np.random.random() < epsilon:
            return np.random.randint(0, espaco_acoes)

        q_values = [self.q_value(estado, acao) for acao in acoes]
        
        # normaliza Q-values de [-1, 1] para [0, 1]
        q_values = (q_values + 1) / 2

        # normaliza Q-values de [0, 1] para [-1, 1]
        q_values = (q_values * 2) - 1

        q_values = np.array(q_values)

        return np.argmax(q_values)

    def treino(self, episodios = 256, batch_size = 64, epsilon = 1.0, epsilon_decay = 0.99,
                   taxa_aprendizado = 0.0002, gamma = 0.95):
        """
            Realiza o treinamento do Agente.
        """
        eps = epsilon
        estat_reforcos = dict()

        for episodio in range(1, episodios + 1):
            estado = [None] * batch_size 
            acao = [None] * batch_size  
            Q_target = np.zeros((batch_size, 1))            
            reforco_acumulado = 0
            
            jogo = AdmiravelMundoNovo()

            for passo in range(batch_size):
                estado_texto, acao_texto, dimensao_acao, reforco, terminado = jogo.read()
                estado_ = self.transforma(estado_texto)
                acao_ = self.transforma(acao_texto)
                
                escolha = self.acao(estado, acao, eps, dimensao_acao)                       

                proximo_estado_texto, proxima_acao_texto, prox_dimensao_acao, reforco, terminado = jogo.simulacao()
                proximo_estado = self.transforma(proximo_estado_texto)
                proxima_acao = self.transforma(proxima_acao_texto) 

                target = reforco + gamma * self.acao(proximo_estado, proxima_acao, eps, prox_dimensao_acao)

                estado[passo] = estado_
                acao[passo] = acao_[escolha]
                Q_target[passo] = target                               
                reforco_acumulado += reforco        

                if terminado:
                    break

                jogo.transicao_estado(escolha)

            estado = pad_sequences(estado)
            acao = pad_sequences(acao)

            self.modelo.fit([estado, acao], Q_target, epochs = 1, verbose = False)

            print("Episódio {0}: Reforço acumulado de {1}".format(episodio, reforco_acumulado))
            estat_reforcos = {episodio: reforco_acumulado}
            eps *= epsilon_decay


if __name__ == '__main__':
    agente = DeepQLearningAgente()
    agente.treino()
