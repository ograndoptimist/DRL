from simulador import AdmiravelMundoNovo
import numpy as np
from keras import Input
from keras.models import Model
from keras.layers import concatenate, Embedding, Dense, Dropout, LSTM
from keras.optimizers import RMSprop
from keras.preprocessing.sequence import pad_sequences
from keras.utils import plot_model
from utilidades import preprocessamento, tokenizacao, palavraParaIndice, vetorizacao
import matplotlib.pyplot as plt

class DeepQLearningAgente(object):
    """
        Implementação de um Agente Artificial utilizando-se de Deep Reinforcement Learning.
        É utilizado o algoritmo off-policy Deep Q-Learning para treinar um Agente baseado em Rede Neural Reccorrente(LSTM).
    """
    def __init__(self):
        with open('vocabulario.txt', 'r') as arquivo:
            vocabulario = arquivo.read()
            vocabulario = ''.join(vocabulario)
            vocabulario = vocabulario.split()
            self.dicionario_de_tokens = palavraParaIndice(vocabulario)
                        
        self.modelo = self.cria_modelo()

        plot_model(self.modelo, show_shapes = True, to_file = 'modelo.png')

    def cria_modelo(self, dimensoes_embedding = 32, dimensoes_lstm = 32, dropout_rate = 0.5, numero_maximo_palavras = 269):
        """
            Implementa a Rede Neural que dá o Q(s,a) para todas possíveis ações no estado considerado.
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
        
        output = Dense(1, activation = 'relu')(fusao)

        modelo = Model([estado, acao], output)

        optimizer = RMSprop(lr = 0.0001)

        modelo.compile(optimizer = optimizer, loss = 'mse', metrics = ['acc'])

        return modelo           

    def transforma(self, texto):
        """
            Realiza a conversão dos textos, que descrevem os estados e as ações, em vetor de inteiros para
            de forma a permitir o aprendizado a camada Embedding.
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
            Retorna o Q(s, a) da ação fornecida associado ao estado.
                ::estado:
                        Um vetor de inteiros.
                ::acao:
                        Um vetor de inteiros
                ::retorna:
                        Um valor numérico racional.
        """
        estado = np.array(estado)
        acao = np.array(acao)
        return self.modelo.predict([estado.reshape((1, len(estado))), acao.reshape((1, len(acao)))])[0][0]      

    def acao(self, estado, acoes, epsilon, espaco_acoes, mode):
        """
            Seletor de ações.
            ::estado:
                    Um vetor de inteiros.
            ::acoes:
                    Um vetor de inteiros.
            ::epsilon:
                    Probabilidade de escolher uma ação aleatória.
            ::retorna::
                    Se mode == 0, retorna o índice de uma ação.
                    Se mode == 1, retorna o Q(s, a).
        """
        if not mode:
            if np.random.random() < epsilon:
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

        return np.argmax(q_values) if mode == 0 else (max(q_values) if isinstance(q_values, np.ndarray) and q_values.ndim != 0 else q_values)       

    def treino(self, episodios = 256, batch_size = 64, epsilon = 1.0, epsilon_decay = 0.99,
                   gamma = 0.95):
        """
            Realiza o treinamento do Agente em batch.
            ::batch_size:
                        Números de experiências que serão usados para o treinamento (cada uma é executada apenas uma vez).
            ::epsilon:
                        Probabilidade de escolher aleatoriamente uma ação.
            ::epsilon_decay:
                        Taxa na qual o epsilon decai (a cada episódio, eps *= epsilon_decay).
            ::gamma:
                        Fator de desconto (gamma alto ~~ reforços futuros valem mais que os reforços imediatos).
            ::retorna:
                        Retorna um dicionário onde {episódio:reforco_acumulado}.            
        """
        eps = epsilon

        # Dicionário que armazena {episódio:reforco_acumulado}
        estat_reforcos = dict()

        for episodio in range(1, episodios + 1):
            estado = [None] * batch_size 
            acao = [None] * batch_size  
            Q_target = np.zeros((batch_size, 1))            
            reforco_acumulado = 0
            cont = 0
            terminado = False

            # O jogo é inicializado no primeiro estado.
            jogo = AdmiravelMundoNovo()

            for passo in range(batch_size):
                # Obtém as descrições de estado e ação do jogo.
                estado_texto, acao_texto, dimensao_acao = jogo.read()

                # Pré-processa os estados e ações, que estão em texto, para vetores de inteiros.
                estado_ = np.array(self.transforma(estado_texto))
                acao_ = np.array(self.transforma(acao_texto))

                # Seleciona uma ação, escolhida de forma aleatória ou através de max(Q(s, a)).
                escolha = self.acao(estado_, acao_, eps, dimensao_acao, mode = 0)
                
                # Executa a ação no emulador e observa o reforço e o próximo estado.
                proximo_estado_texto, proximas_acoes_texto, prox_dimensao_acao, prox_reforco, terminado = jogo.emulador(escolha)

                # Pré-processa os próximos estados e ações, que estão em texto, para vetores de inteiros.
                proximo_estado = self.transforma(proximo_estado_texto)
                proximas_acoes = self.transforma(proximas_acoes_texto)

                if not terminado:
                    # Q(s, a) = r' +  γ  * Q(s', a')
                    target = prox_reforco + gamma * self.acao(proximo_estado, proximas_acoes, eps, prox_dimensao_acao, mode = 1)
                else:
                    target = prox_reforco

                # Para o treinamento ser realizado em batch, é necessário que:
                estado[cont] = estado_
                acao[cont] = acao_[escolha]
                Q_target[cont] = target                               
                reforco_acumulado += prox_reforco

                if terminado:
                    break

                # Dessa vez, a transição de estado é realizada:
                # estado = novo_estado
                jogo.transicao_estado(escolha)

                cont += 1

            # As sequências precisam ter o mesmo tamanho dentro do mesmo tensor.    
            estado = pad_sequences(estado[:cont + 1])
            acao = pad_sequences(acao[:cont + 1])
            
            np.random.seed(0)

            # Realiza o passo de gradiente de descida de forma a alcançar o mínimo global da função.
            self.modelo.fit([estado, acao], Q_target[:cont + 1], epochs = 1, verbose = False)

            print("Episódio {0}: Reforço acumulado de {1}".format(episodio, reforco_acumulado))

            estat_reforcos.update({episodio: reforco_acumulado})
            eps *= epsilon_decay

        # Salva o modelo da rede neural utilizada.
        self.modelo.save('modelo_lstm')

        return estat_reforcos         


if __name__ == '__main__':
    agente = DeepQLearningAgente()
    teste = agente.treino()

    plt.plot(teste.keys(), teste.values())
    plt.title('Agente de Treino: Episodios x Reforços')
    plt.xlabel('Episodios')
    plt.ylabel('Reforços Acumulados')
    plt.savefig('treino.png')
