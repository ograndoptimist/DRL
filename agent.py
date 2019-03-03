from simulador import AdmiravelMundoNovo
import numpy as np
from keras.models import Sequential
from keras.layers import Embedding, Dense, LSTM


def preprocessamento(texto: str):
    """
        Elimina pontuação, aspas simples e duplas do texto.
        ::parametros:
                texto: uma string que contém todo o texto.
        ::retorno:
                returns a string containing all of the words from the original string but without
                especial symbols and capital letters.
        Exemplo:
            >>> preprocessamento("Algum texto aleatorio, aqui.")
            'algum texto aleatorio aqui'
    """

    texto_preprocessado = ''

    texto = list(texto.lower().split())
        
    for palavra in texto:
        nova_palavra = ''
        for caracter in palavra:
            if caracter in {".", ",", "'", "’", '"', ":", "!"}:
                pass
            else:
                nova_palavra += caracter
        texto_preprocessado +=  ' ' + nova_palavra

    texto_preprocessado = texto_preprocessado.replace('\\t', ' ').replace('\\n', ' ')

    return texto_preprocessado.lower()

def tokenizacao(texto_preprocessado: str):
    """
        Constrói a tokenização.
        ::parametros:
                texto_preprocessado: o texto pré-processado a ser tokenizado.
        ::retorno:
                retorna um vetor de tokens.
        Exemplo:
            >>> tokenizacao("algum texto aleatorio aqui")
            ['algum', 'texto', 'aleatorio', 'aqui']
    """

    raw_words = texto_preprocessado.split()

    token = []

    for palavra in raw_words:
        if palavra not in token:
            token.append(palavra)

    return token


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
