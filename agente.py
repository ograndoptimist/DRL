from simulador import AdmiravelMundoNovo
import numpy as np
from keras.models import Sequential
from keras.layers import Embedding, Dense, LSTM
from utilidades import preprocessamento, tokenizacao, palavraParaIndice, vetorizacao
import random



class DeepQLearningAgent(object):
    """
        Implementação de um Agente Artificial utilizando-se de Reinforcement Learning e Deep Learning.
        É utilizado o algoritmo off-policy Q-Learning para treinar uma Rede Neural baseada em LSTM.
    """
    def __init__(self, dimensoes_embedding, dimensoes_lstm):
        with open('vocabulario.txt', 'r') as arquivo:
            vocabulario = arquivo.read()
            vocabulario = list(vocabulario.split())
            tokens = tokenizacao(vocabulario)
            self.dicionario_de_tokens = palavraParaIndice(tokens)

        self.model = self.modelo(dimensoes_embedding, dimensoes_lstm)

    def modelo(self, dimensoes_embedding = 16, dimensoes_lstm = 32, numero_maximo_palavras = 269):
        """
            Implementa a rede neural que escolhe a ação a ser realizada no corrente estado.
        """
        model = Sequential()

        model.add(Embedding(numero_maximo_palavras, dimensoes_embedding))
        model.add(LSTM(dimensoes_lstm))
        model.add(Dense(8, activation = 'tanh'))        

        model.compile(optimizer = 'rmsprop', loss_function = 'mse', metrics = ['acc'])
        
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

    def q_value(self, estado, acao):
        """
            Alimenta o modelo com um estado e uma ação, de forma a obter na saída o Q(s, a).
                ::estado:
                ::acao:
        """
        return self.model.predict([estado + acao])        

    def acao(estado, acoes, epsilon, funcao_historico):
        """
            Seletor de ações.
            ::estado:
            ::acoes:
            ::epsilon:
                Probabilidade de escolher uma ação aleatória.
            ::historico:
                retorna um valor igual ao número de vezes o agente selecionou a ação a no estado s na atual execução.
                o histórico penaliza os pares estado-ação já visitados.
        """
    
        if np.random.random() < epsilon:
            return random.randint(0, len(espaco_acoes) + 1)

        q_values = [self.q_value(estado, acao) for acao in acoes]

        # normaliza Q-values de [-1, 1] para [0, 1]
        q_values = (q_values + 1) / 2

        # Aplica a função histórico
        q = funcao_historico(s, a) + 1 for q in q_values

        # normaliza Q-values de [0, 1] para [-1, 1]
        q_values = (q_values * 2) - 1

        return max(q_values)

    def treino(self, episodios = 256: int, epsilon = 1.0: float, epsilon_decay = 0.99: float,
                   taxa_aprendizado = 0.0002: float, gamma = 0.95: float):
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
                if epsilon < np.random.random():
                    acao = np.random.randint(dimensao_acao)
                else:
                    acao = self.model.predict(estado)

                proximo_estado_texto, proxima_acao_texto, reforco, prox_dimensao_acao, terminado = jogo.transicao_estado(acao)
                proximo_estado, proxima_acao = self.transforma(proximo_estado_texto, proxima_acao_texto)                

                Q_target = reforco + gamma * self.Q(proximo_estado, proxima_acao)

                self.model.fit(estado, Q_target, epochs = 10, verbose = False)

                estado = proximo_estado
                acao = proxima_acao
                dimensao_acao = prox_dimensao_acao
                eps *= epsilon_decay
                reforco_acumulado += reforco

            print("Episódio {0}: Reforço acumulado de {1}".format(episodio, reforco_acumulado))
            estat_reforcos = {episodio: reforco_acumulado}

    def Q(self, estado, acao):
        """
            Retorna a ação de maior Q-value.
        """        
        pass


if __name__ == '__main__':
    agente = DeepQLearningAgente()
    agente.treino()
