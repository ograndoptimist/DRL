from simulador import AdmiravelMundoNovo
import numpy as np
from keras.models import Sequential
from keras.layers import Embedding, Dense, Dropout, LSTM
from utilidades import preprocessamento, tokenizacao, palavraParaIndice, vetorizacao
import random



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
            
        self.model = self.modelo()

    def modelo(self, dimensoes_embedding = 16, dimensoes_lstm = 32, numero_maximo_palavras = 269, dropout_rate = 0.5):
        """
            Implementa a rede neural que escolhe a ação a ser realizada no corrente estado.
        """
        model = Sequential()

        model.add(Embedding(numero_maximo_palavras, dimensoes_embedding))
        model.add(Dropout(dropout_rate))
        model.add(LSTM(dimensoes_lstm))
        model.add(Dense(8, activation = 'tanh'))        

        model.compile(optimizer = 'rmsprop', loss = 'mse', metrics = ['acc'])
        
        return model

    def transforma(self, texto):
        """
            Realiza a conversão dos textos que descrevem os estados e as ações em vetor de inteiros.
        """
        if isinstance(texto, list):
            texto = ' '.join(texto)

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
        return self.model.predict([estado + acao])        

    def acao(self, estado, acoes, epsilon, espaco_acoes):
        """
            Seletor de ações.
            ::estado:
            ::acoes:
            ::epsilon:
                Probabilidade de escolher uma ação aleatória.
        """
    
        if np.random.random() < epsilon:
            return random.randint(0, len(espaco_acoes) + 1)

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
            jogo = AdmiravelMundoNovo()

            estado_texto, acao_texto, reforco, dimensao_acao, terminado = jogo.read()
            estado = self.transforma(estado_texto)
            acao = self.transforma(acao_texto)

            reforco_acumulado = 0
            while not terminado:
                acao = self.acao(estado, acao, eps, dimensao_acao)

                proximo_estado_texto, proxima_acao_texto, reforco, prox_dimensao_acao, terminado = jogo.transicao_estado(acao)
                proximo_estado, proxima_acao = self.transforma(proximo_estado_texto, proxima_acao_texto)                

                Q_target = reforco + gamma * self.acao(proximo_estado, proxima_acao, eps, prox_dimensao_acao)

                self.model.fit(estado, Q_target, epochs = 10, batch_size = batch_size, verbose = False)

                estado = proximo_estado
                acao = proxima_acao
                dimensao_acao = prox_dimensao_acao
                reforco_acumulado += reforco

            print("Episódio {0}: Reforço acumulado de {1}".format(episodio, reforco_acumulado))
            estat_reforcos = {episodio: reforco_acumulado}
            eps *= epsilon_decay


if __name__ == '__main__':
    agente = DeepQLearningAgente()
    agente.treino()
