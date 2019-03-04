from simulador import AdmiravelMundoNovo
import time
import random
from utilidades import preprocessamento


class AgenteAleatorio(object):
    def __init__(self):
        self.vocabulario = ""
        self.joga()
        
    def joga(self, episodios = 100):
        self.vocab = ""
        for episodio in range(1, episodios + 1):
            jogo = AdmiravelMundoNovo()

            estado, lista_acoes, espaco_acoes, reforco_imediato, terminado = jogo.read()
            print("\tReforço: {0}".format(reforco_imediato))
            print(estado)
            jogo.imprimeAcao(lista_acoes)
            
            self.vocabulario += ' ' + (estado + ' ' + ' '.join(lista_acoes) + " Reforço: %d" %reforco_imediato)
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

                self.vocabulario += ' ' + (estado + ' ' + ' '.join(lista_acoes) + " Reforço: %d" %reforco_imediato)
            
            print()

        
    def gera_vocabulario(self):
        self.vocabulario = preprocessamento(self.vocabulario)
        lista_vocabulario = set(self.vocabulario.split())

        with open('vocab_teste.txt', 'w') as arquivo:
            for palavra in lista_vocabulario:
                arquivo.write("%s\n" %palavra)        


if __name__ == '__main__':
    teste = AgenteAleatorio()
    teste.gera_vocabulario()
