from simulador import AdmiravelMundoNovo
import numpy as np
from keras.models import Sequential
from keras.layers import Embedding, Dense, LSTM
from utilidades import preprocessamento, tokenizacao, palavraParaIndice, vetorizacao



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
        model.add(Dense(8))        

        model.compile(optimizer = 'rmsprop', loss_function = '', metrics = ['acc'])
        
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

    def treino(self, episodios: int, epsilon: float, epsilon_decay: float, taxa_aprendizado: float, fator_desconto: float):
        """
            Realiza o treinamento do Agente.
        """
        eps = epsilon
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

                target = reforco + fator_desconto * self.Q(proximo_estado, proxima_acao)

                self.model.fit(estado, target, epochs = 10, verbose = False)

                estado = proximo_estado
                acao = proxima_acao
                dimensao_acao = prox_dimensao_acao
                eps *= epsilon_decay
                reforco_acumulado += reforco

            print("Episódio {0}: Reforço acumulado de {1}".format(episodio, reforco_acumulado))

    def Q(self, estado, acao):
        pass
