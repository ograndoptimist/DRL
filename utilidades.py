def preprocessamento(texto):
    """
        Elimina pontuação e símbolos especiais do texto.
        ::parametros:
                texto: uma string que contém todo o texto.
        ::retorno:
                retorna uma string contendo todas palavras do string original mas sem
                símbolos especiais e letras maiúsculas.
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
            elif caracter in ['á', 'â', 'ã', 'à']:
                nova_palavra += 'a'
            elif caracter in ['é', 'ê']:
                nova_palavra += 'e'
            elif caracter in ['ó', 'ô', 'õ']:
                nova_palavra += 'o'
            elif caracter == 'í':
                nova_palavra += 'i'
            elif caracter == 'ú':
                nova_palavra += 'u'
            else:
                nova_palavra += caracter
        texto_preprocessado +=  ' ' + nova_palavra

    texto_preprocessado = texto_preprocessado.replace('\\t', ' ').replace('\\n', ' ')

    return texto_preprocessado.lower()

def tokenizacao(texto_preprocessado):
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

def palavraParaIndice(tokens):
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

def vetorizacao(lista_de_palavras, dicionario_de_palavras):
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
