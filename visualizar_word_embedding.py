import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
from keras.models import load_model, Sequential
from keras.layers import Embedding
from utilidades import vetorizacao, palavraParaIndice
     
def main():     
    wv, vocabulary = load_embeddings()
    
    wv = wv.reshape(272, 32)
     
    tsne = TSNE(n_components = 2, random_state = 0)
    np.set_printoptions(suppress = True)
    Y = tsne.fit_transform(wv)
     
    plt.scatter(Y[:, 0], Y[:, 1])
    for label, x, y in zip(vocabulary, Y[:, 0], Y[:, 1]):
        plt.annotate(label, xy = (x, y), xytext = (0, 0), textcoords = 'offset points')

    plt.show()
     
     
def load_embeddings():
    modelo = load_model('modelo_lstm')
    embedding_weights = modelo.layers[2].weights

    modelo_embedding = Sequential()
    modelo_embedding.add(Embedding(272, 32))

    modelo_embedding.layers[0].set_weights = embedding_weights

    with open('vocabulario.txt', 'r') as arquivo:
        vocabulario = arquivo.read()

    vocabulario = list(vocabulario.split())
    dicionario_de_palavras = palavraParaIndice(vocabulario)
    vetor_palavras = vetorizacao(vocabulario, dicionario_de_palavras)
    
    teste = np.zeros((272, 1, 32))
    for i, palavra in enumerate(vetor_palavras):
        teste[i] = modelo_embedding.predict([palavra])   
    
    return teste, vocabulario

         
if __name__ == '__main__':
    main()
    
