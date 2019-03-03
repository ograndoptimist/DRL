from simulador import AdmiravelMundoNovo
import numpy as np
from keras.models import Sequential
from keras.layers import Embedding, Dense, LSTM


class DeepQLearningAgent(object):
    def __init__(self):
        self.model = self.modelo()

    def modelo(self):
        
        return model

    def treino(self, episodios, epsilon, epsilon_decay):
        for episodio in range(1, episodios + 1):
            eps = epsilon
            jogo = AdmiravelMundoNovo()
            estado, acao, reforco, terminado = jogo.read()
            while not terminado:
                if epsilon < np.random.random():
                    executa =
                else:
                    target = 
                    self.model.fit(estado, target, epochs = 10, verbose = False)
                    acao = self.model.predict(estado)
                proximo_estado, proxima_acao, reforco, terminado = jogo.transicao_estado(acao)
                eps *= epsilon_decay
                
                
            
        
