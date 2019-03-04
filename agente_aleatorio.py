from simulador import AdmiravelMundoNovo
import time
import random


class AgenteAleatorio(object):
    def __init__(self):
        self.joga()
        
    def joga(self, episodios = 10):
        for episodio in range(1, episodios + 1):
            jogo = AdmiravelMundoNovo()

            estado, lista_acoes, espaco_acoes, reforco_imediato, terminado = jogo.read()
            print("\tReforço: {0}".format(reforco_imediato))
            print(estado)
            jogo.imprimeAcao(lista_acoes)
            while not terminado:
                time.sleep(3)

                acao = random.randint(0, espaco_acoes - 1)
                print("\t>>> ", acao)
                print()
                
                jogo.transicao_estado(acao)
                estado, lista_acoes, espaco_acoes, reforco_imediato, terminado = jogo.read()

                print("\tReforço: {0}".format(reforco_imediato))
                print(estado)
                jogo.imprimeAcao(lista_acoes)

            print()


if __name__ == '__main__':
    teste = AgenteAleatorio()
    

                
                
                
                
        
        
