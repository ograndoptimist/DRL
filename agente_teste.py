"""
    Teste de generalização do modelo.
"""
from agente_treino import DeepQLearningAgente
from simulador import AdmiravelMundoNovo
import time
import matplotlib.pyplot as plt
from keras.models import load_model
import numpy as np

class AgenteTeste(DeepQLearningAgente):
    def __init__(self):
        super().__init__()
        self.modelo = load_model('modelo_lstm')

    def politica(self, estado, acoes):
        estado = np.array(estado)

        if isinstance(acoes[0], int):
            acao = np.array(acoes)
            q_values = self.modelo.predict([estado.reshape((1, len(estado))), acao.reshape((1, len(acao)))])[0][0]
        else:
            q_values = []
            for acao in acoes:
                acao = np.asarray(acao)
                q_values.append(self.modelo.predict([estado.reshape((1, len(estado))), acao.reshape((1, len(acao)))])[0][0])

        return np.argmax(q_values)
        
    def joga(self, episodios = 256):
        estat_reforcos = dict()
        
        for episodio in range(1, episodios + 1):
            jogo = AdmiravelMundoNovo()
            reforco_acumulado = 0
            
            estado, lista_acoes, espaco_acoes, reforco_imediato, terminado = jogo.read_1()
            print("\tReforço: {0}".format(reforco_imediato))
            print(estado)
            jogo.imprimeAcao(lista_acoes)
            
            while not terminado:
                reforco_acumulado += reforco_imediato
                time.sleep(3)

                estado_ = self.transforma(estado)
                lista_acoes_ = self.transforma(lista_acoes)
                acao = self.politica(estado_, lista_acoes_)
                print("\t>>> ", acao)
                print()

                jogo.transicao_estado(acao)
                estado, lista_acoes, espaco_acoes, reforco_imediato, terminado = jogo.read_1()

                print("\tReforço: {0}".format(reforco_imediato))
                print(estado)
                jogo.imprimeAcao(lista_acoes)                
                            
            print("Episódio {0}: Reforço acumulado de {1}".format(episodio, reforco_acumulado))
            estat_reforcos.update({episodio: reforco_acumulado})

        return estat_reforcos     


if __name__ == '__main__':
    t = AgenteTeste()
    teste = t.joga()   

    plt.plot(teste.keys(), teste.values())
    plt.title('Agente Aleatório')
    plt.xlabel('Episodios')
    plt.ylabel('Reforços Acumulados')
    plt.savefig('teste_aleatorio.png')
