from simulador import AdmiravelMundoNovo
import numpy as np
from keras.models import Sequential
from keras.layers import Embedding, Dense, LSTM


def preprocessText(text: str):
    """
        Eliminate pontuactions, single and double quoted symbols from the current string.
        ::params:
                text: a string containg all the suplemented text.
        ::return:
                returns a string containing all of the words from the original string but without
                especial symbols and capital letters.
        Example:
            >>> eliminatePontuaction("Some random text.")
            'some random text here'
    """

    preprocessed_text = ''

    text = list(text.lower().split())
        
    for word in text:
        new_word = ''
        for character in word:
            if character in {".", ",", "'", "’", '"', ":", "!"}:
                pass
            else:
                new_word += character
        preprocessed_text +=  ' ' + new_word

    preprocessed_text = preprocessed_text.replace('\\t', ' ').replace('\\n', ' ')

    return preprocessed_text.lower() 


class DeepQLearningAgent(object):
    def __init__(self):
        self.model = self.modelo()

    def modelo(self, estado_texto, acao_texto, dimensoes_embedding = 16, dimensoes_lstm = 32, numero_maximo_palavras):
        model = Sequential()

        model.add(Embedding(numero_maximo_palavras, dimensoes_embedding))
        model.add(LSTM(dimensoes_lstm))
        model.add(Dense(8))        

        model.compile(optimizer = 'rmsprop', loss_function = '', metrics = '')
        
        return model

    def treino(self, episodios, epsilon, epsilon_decay):
        for episodio in range(1, episodios + 1):
            eps = epsilon
            jogo = AdmiravelMundoNovo()
            estado, acao, reforco, terminado = jogo.read()
            while not terminado:
                if epsilon < np.random.random():
                    pass
                    executa =
                else:
                    acao = self.model.predict(estado)
                proximo_estado, proxima_acao, reforco, terminado = jogo.transicao_estado(acao)
                target = self.Q(estado, acao) + learning_rate * [self.Q(proximo_estado, proxima_acao) - self.Q(estado, acao)]
                self.model.fit(estado, target, epochs = 10, verbose = False)
                eps *= epsilon_decay

    def Q(self, estado, acao):
        pass
