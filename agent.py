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

def palavraParaIndice(tokens: list[str]):
    """
        Cria um dicionário associando um índice inteiro a cada palavra no vetor tokens.
        ::parametros:
            tokens: um vetor de palavras únicas.
        ::retorno:
            dicionario_de_palavra: retorna um dicionario contendo  todo o vocabulário composto
            do seguinte conteúdo: {'palavra': índice_inteiro}.
         Exemplo:
            >>> palavraParaIndice(['algum', 'texto', 'aleatorio', 'aqui'])
            {'algum': 0, 'texto': 1, 'aleatorio': 2, 'aqui': 3}
    """

    dicionario_de_palavras = dict()

    for indice, palavra in enumerate(tokens):
        dicionario_de_palavras[palavra] = indice

    return dicionario_de_palavras

def vectorizacao(lista_de_palavras: list[str], dicionario_de_palavras: dict[str:int]):
    """
        Vetorização dos tokens.
        ::parametros:
            lista_de_palavras: um vetor com as palavras pré-processadas.
            dicionario_de_palavras: um dicionário contendo todo o vocabulário do texto.
        ::retorna:
            retorna um vetor de inteiros contendo o índice de cada palavra do texto.
        Exemplo:
            >>> vetorizacao(['algum', 'texto', 'aleatorio', 'aqui'], {'algum': 0, 'texto': 1, 'aleatorio': 2, 'aqui': 3})
            [0, 1, 2, 3]
    """

    vetor = []

    for palavra in lista_de_palavras:
        vetor.append(dicionario_de_palavras[palavra])

    return vetor 



class DeepQLearningAgent(object):
    def __init__(self, dimensoes_embedding, dimensoes_lstm):
        with open('vocabulario.txt', 'r') as arquivo:
            vocabulario = arquivo.read()
            vocabulario = list(vocabulario.split())
            tokens = tokenizacao(vocabulario)
            self.dicionario_de_tokens = palavraParaIndice(tokens)

        self.model = self.modelo(dimensoes_embedding, dimensoes_lstm)

    def modelo(self, dimensoes_embedding = 16: int, dimensoes_lstm = 32: int, numero_maximo_palavras = 269: int):
        model = Sequential()

        model.add(Embedding(numero_maximo_palavras, dimensoes_embedding))
        model.add(LSTM(dimensoes_lstm))
        model.add(Dense(8))        

        model.compile(optimizer = 'rmsprop', loss_function = '', metrics = ['acc'])
        
        return model

    def transforma(self, estado_texto:str, acao_texto: list[str]):
        estado_texto = preprocessamento(estado_texto)
        estado_texto = tokenizacao(estado_texto)
        estado_texto = vetorizacao(estado_texto, self.dicionario_de_tokens)

        acao_texto = preprocessamento(acao_texto)
        acao_texto = tokenizacao(acao_texto)
        acao_texto = vetorizacao(acao_texto, self.dicionario_de_tokens)

        return estado_texto, acao_texto        

    def treino(self, episodios: int, epsilon: float, epsilon_decay: float, taxa_aprendizado: float, fator_desconto: float):
        eps = epsilon
        for episodio in range(1, episodios + 1):
            jogo = AdmiravelMundoNovo()

            estado_texto, acao_texto, reforco, dimensao_acao, terminado = jogo.read()
            estado, acao = self.transforma(estado_texto, acao_texto)

            reforco_acumulado = 0
            while not terminado:
                if epsilon < np.random.random():
                    acao = np.random.randint(dimensao_acao)
                else:
                    acao = self.model.predict(estado)

                proximo_estado_texto, proxima_acao_texto, proximo_reforco, prox_dimensao_acao, terminado = jogo.transicao_estado(acao)
                proximo_estado, proxima_acao = self.transforma(proximo_estado_texto, proxima_acao_texto)                

                target = proximo_reforco + fator_desconto * self.Q(proximo_estado, proxima_acao)

                self.model.fit(estado, target, epochs = 10, verbose = False)

                estado = proximo_estado
                acao = proxima_acao
                dimensao_acao = prox_dimensao_acao

                eps *= epsilon_decay
                reforco_acumulado += reforco

    def Q(self, estado: list[int], lista_acoes: list[int]):
        pass
