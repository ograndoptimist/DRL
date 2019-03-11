from simulador import AdmiravelMundoNovo
import numpy as np
from keras import Input
from keras.models import Model
from keras.layers import concatenate, Embedding, Dense, Dropout, LSTM
from keras.preprocessing.sequence import pad_sequences
from utilidades import preprocessamento, tokenizacao, palavraParaIndice, vetorizacao
import matplotlib.pyplot as plt



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

    def cria_modelo(self, dimensoes_embedding = 32, dimensoes_lstm = 32, dropout_rate = 0.5, numero_maximo_palavras = 269):
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

        camada_dropout = Dropout(dropout_rate)(fusao)
        
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

    def q_value(self, estado_q_value, acao_q_value, epsilon):
        """
            Alimenta o modelo com um estado e uma ação, de forma a obter na saída o Q(s, a).
                ::estado:
                ::acao:
        """
        estado_q_value = np.array(estado_q_value)
        acao_q_value = np.array(acao_q_value)
        return self.modelo.predict([estado_q_value.reshape((1, len(estado_q_value))), acao_q_value.reshape((1, len(acao_q_value)))])[0][0]      

    def acao(self, estado, acoes, epsilon, espaco_acoes, mode):
        """
            Seletor de ações.
            ::estado:
            ::acoes:
            ::epsilon:
                Probabilidade de escolher uma ação aleatória.
        """
        if mode == 0:
            if np.random.random() < epsilon:
                if espaco_acoes in [0, 1]:
                    return 0
                else:
                    return np.random.randint(0, espaco_acoes)

            estado_acao = np.array(estado)
            acoes_acao = np.array(acoes)

            q_values = self.q_value(estado, acoes[0], epsilon) if len(acoes) == 1 else [self.q_value(estado, acao, epsilon) for acao in acoes]        
        else:
            if len(acoes) == 0:
                return 0
            elif len(acoes) == 1: 
                q_values =  self.q_value(estado, acoes[0], epsilon)
            else:
                q_values = [self.q_value(estado, acao, epsilon) for acao in acoes]
                    
        q_values = np.array(q_values)
        
        # normaliza Q-values de [-1, 1] para [0, 1]
        q_values = (q_values + 1) / 2

        # normaliza Q-values de [0, 1] para [-1, 1]
        q_values = (q_values * 2) - 1

        return np.argmax(q_values) if mode == 0 else (max(q_values) if isinstance(q_values, np.ndarray) else q_values)       

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
            cont = 0

            jogo = AdmiravelMundoNovo()

            for passo in range(batch_size):
                estado_texto, acao_texto, dimensao_acao, reforco, terminado = jogo.read()
                estado_ = self.transforma(estado_texto)
                acao_ = self.transforma(acao_texto)

                escolha = self.acao(estado_, acao_, eps, dimensao_acao, mode = 0)
                                
                proximo_estado_texto, proximas_acoes_texto, prox_dimensao_acao, reforco, terminado = jogo.simulacao(escolha)
                proximo_estado = self.transforma(proximo_estado_texto)
                proximas_acoes = self.transforma(proximas_acoes_texto)
                
                target = reforco + gamma * self.acao(proximo_estado, proximas_acoes, eps, prox_dimensao_acao, mode = 1)
                
                estado[passo] = estado_
                acao[passo] = acao_[escolha]
                Q_target[passo] = target                               
                reforco_acumulado += reforco        

                if terminado:
                    break

                jogo.transicao_estado(escolha)
                cont += 1
                
            estado = pad_sequences(estado[:cont + 1])
            acao = pad_sequences(acao[:cont + 1])

            self.modelo.fit([estado, acao], Q_target[:cont + 1], epochs = 1, verbose = False)

            print("Episódio {0}: Reforço acumulado de {1}".format(episodio, reforco_acumulado))
            estat_reforcos.update({episodio: reforco_acumulado})
            eps *= epsilon_decay

        return estat_reforcos            


if __name__ == '__main__':
    agente = DeepQLearningAgente()
    teste = agente.treino()

    plt.plot(teste.keys(), teste.values())
    plt.title('Episodios x Reforços')
    plt.xlabel('Episodios')
    plt.ylabel('Reforços Acumulados')
    plt.savefig('teste.png')
