"""
    \tSeja bem-vindo ao Admirável Mundo Novo!
    \tO objetivo do jogo é dar suporte ao desenvolvimento de Agentes Inteligentes que utilizam Deep Reinforcement Learning
    \tpara tarefas de Processamento de Linguagem Natural em língua portuguesa.
    \tAutor: Gabriel Pontes (@ograndoptimist)       
"""

from textos import ESTADOS, ACOES, REFORCOS, FINALIZADO, DIMENSOES
import random

print(__doc__)

class AdmiravelMundoNovo(object):
    def __init__(self):
        self.reforco = 0
        self._checa_estado = False
        self._estado_texto = None
        self._estado_acao = None
        self._finalizado = False
        self._espaco_acoes = None
        self._estados_texto = ESTADOS
        self._acao_textos =  ACOES
        self._acao_dimensoes = DIMENSOES
        self._estados_reforcos = REFORCOS
        self._estados_finalizado = FINALIZADO
        self._valores_estados_iniciais  = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

        print("\tO objetivo do jogo é coletar a chave preciosa de ouro." + 
              ".\n\tPara tal, você precisa vasculhar a Ilha da Fantasia.")
        print()

        self._escolha_estado_inicial()

    def _escolha_estado_inicial(self):
        escolha = random.choice(self._valores_estados_iniciais)

        if escolha == 1:            
            self._estado_1()
        elif escolha == 2:            
            self._estado_2()
        elif escolha == 3:            
            self._estado_3()
        elif escolha == 4:            
            self._estado_4()
        elif escolha == 5:            
            self._estado_5()
        elif escolha == 6:            
            self._estado_6()
        elif escolha == 7:            
            self._estado_7()
        elif escolha == 8:            
            self._estado_8()
        elif escolha == 9:            
            self._estado_9()
        elif escolha == 10:            
            self._estado_10()
        elif escolha == 11:            
            self._estado_11()
        elif escolha == 12:           
            self._estado_12()
        elif escolha == 13:            
            self._estado_13()
        elif escolha == 14:
            self._estado_14()

    def transicao_estado(self, acao):        
        if self._valor_estado == 2 and acao == 0:
            self._estado_6()
        elif self._valor_estado == 2 and acao == 1:
            self._estado_3()
        elif self._valor_estado in [1, 3, 4] and acao == 0:
            self._estado_2()
        elif self._valor_estado == 3 and acao == 1:
            self._estado_5()
        elif self._valor_estado == 2 and acao == 2:
            self._estado_4()
        elif self._valor_estado == 5 and acao == 1:
            self._estado_3()
        elif self._valor_estado == 6 and acao == 1:
            self._estado_7()
        elif self._valor_estado in [7, 8] and acao == 0:
            self._estado_6()
        elif self._valor_estado == 6 and acao == 2:
            self._estado_8()        
        elif self._valor_estado in [6, 10, 11] and acao == 0:
            self._estado_9()
        elif self._valor_estado == 9 and acao == 1: 
            self._estado_10()
        elif self._valor_estado == 9 and acao == 2: 
            self._estado_11()
        elif self._valor_estado in [5, 9, 13] and acao == 0: 
            self._estado_12()
        elif self._valor_estado == 12 and acao == 0:
            self._estado_13()
        elif self._valor_estado == 12 and acao == 1:
            self._estado_final()
        elif self._valor_estado == 9 and acao == 3: 
            self._estado_6()
        elif self._valor_estado == 6 and acao == 3:
            self._estado_2()        
        
    def _estado_1(self):
        self._reforco_imediato = self._estados_reforcos['estado_1']
        self.reforco += self._reforco_imediato
        self._valor_estado = 1
        self._finalizado = self._estados_finalizado['estado_1']
        self._estado_texto = self._estados_texto['estado_1']
        self._estado_acao = self._acao_textos['estado_1']
        self._espaco_acoes = self._acao_dimensoes['estado_1']
                
    def _estado_2(self):
        self._reforco_imediato = self._estados_reforcos['estado_2']
        self.reforco += self._reforco_imediato
        self._valor_estado = 2
        self._finalizado = self._estados_finalizado['estado_1']
        self._estado_texto = self._estados_texto['estado_2']
        self._estado_acao = self._acao_textos['estado_2']
        self._espaco_acoes = self._acao_dimensoes['estado_2']
        
    def _estado_3(self):
        self._reforco_imediato = self._estados_reforcos['estado_3']
        self.reforco += self._reforco_imediato
        self._valor_estado = 3
        self._finalizado = self._estados_finalizado['estado_1']
        self._estado_texto = self._estados_texto['estado_3']
        self._estado_acao = self._acao_textos['estado_3']
        self._espaco_acoes = self._acao_dimensoes['estado_3']
        
    def _estado_4(self):
        self._reforco_imediato = self._estados_reforcos['estado_4']
        self.reforco += self._reforco_imediato
        self._valor_estado = 4
        self._finalizado = self._estados_finalizado['estado_1']
        self._estado_texto = self._estados_texto['estado_4']
        self._estado_acao = self._acao_textos['estado_4']
        self._espaco_acoes = self._acao_dimensoes['estado_4']
        
    def _estado_5(self):
        self._reforco_imediato = self._estados_reforcos['estado_5']
        self.reforco += self._reforco_imediato
        self._valor_estado = 5
        self._finalizado = self._estados_finalizado['estado_1']
        self._estado_texto = self._estados_texto['estado_5']
        self._estado_acao = self._acao_textos['estado_5']
        self._espaco_acoes = self._acao_dimensoes['estado_5']
        
    def _estado_6(self):
        self._reforco_imediato = self._estados_reforcos['estado_6']
        self.reforco += self._reforco_imediato
        self._valor_estado = 6
        self._finalizado = self._estados_finalizado['estado_1']
        self._estado_texto = self._estados_texto['estado_6']
        self._estado_acao = self._acao_textos['estado_6']
        self._espaco_acoes = self._acao_dimensoes['estado_6']
        
    def _estado_7(self):
        self._reforco_imediato = self._estados_reforcos['estado_7']
        self.reforco += self._reforco_imediato
        self._valor_estado = 7
        self._finalizado = self._estados_finalizado['estado_1']
        self._estado_texto = self._estados_texto['estado_7']
        self._estado_acao = self._acao_textos['estado_7']
        self._espaco_acoes = self._acao_dimensoes['estado_7']
        
    def _estado_8(self):
        self._reforco_imediato = self._estados_reforcos['estado_7']
        self.reforco += self._reforco_imediato
        self._valor_estado = 8
        self._finalizado = self._estados_finalizado['estado_1']
        self._estado_texto = self._estados_texto['estado_8']
        self._estado_acao = self._acao_textos['estado_7']
        self._espaco_acoes = self._acao_dimensoes['estado_7']
        
    def _estado_9(self):
        self._reforco_imediato = self._estados_reforcos['estado_9']
        self.reforco += self._reforco_imediato
        self._valor_estado = 9
        self._finalizado = self._estados_finalizado['estado_1']
        self._estado_texto = self._estados_texto['estado_9']
        self._estado_acao = self._acao_textos['estado_9']
        self._espaco_acoes = self._acao_dimensoes['estado_9']
        
    def _estado_10(self):
        self._reforco_imediato = self._estados_reforcos['estado_10']
        self.reforco += self._reforco_imediato
        self._valor_estado = 10
        self._finalizado = self._estados_finalizado['estado_1']
        self._estado_texto = self._estados_texto['estado_10']
        self._estado_acao = self._acao_textos['estado_10']
        self._espaco_acoes = self._acao_dimensoes['estado_10']
        
    def _estado_11(self):
        self._reforco_imediato = self._estados_reforcos['estado_10']
        self.reforco += self._reforco_imediato
        self._valor_estado = 11
        self._finalizado = self._estados_finalizado['estado_1']
        self._estado_texto = self._estados_texto['estado_11']
        self._estado_acao = self._acao_textos['estado_10']
        self._espaco_acoes = self._acao_dimensoes['estado_10']
        
    def _estado_12(self):
        self._reforco_imediato = self._estados_reforcos['estado_12']
        self.reforco += self._reforco_imediato
        self._valor_estado = 12
        self._finalizado = self._estados_finalizado['estado_1']
        self._estado_texto = self._estados_texto['estado_12']
        self._estado_acao = self._acao_textos['estado_12']
        self._espaco_acoes = self._acao_dimensoes['estado_12']
        
    def _estado_13(self):
        self._reforco_imediato = self._estados_reforcos['estado_13']
        self.reforco -= self._reforco_imediato
        self._valor_estado = 13
        self._finalizado = self._estados_finalizado['estado_1']
        self._estado_texto = self._estados_texto['estado_13']
        self._estado_acao = self._acao_textos['estado_13']
        self._espaco_acoes = self._acao_dimensoes['estado_13']

    def _estado_14(self):
        self._reforco_imediato = self._estados_reforcos['estado_14']
        self.reforco -= self._reforco_imediato
        self._valor_estado = 14
        self._finalizado = self._estados_finalizado['estado_14']
        self._estado_texto = self._estados_texto['estado_14']
        self._estado_acao = self._acao_textos['estado_14']
        self._espaco_acoes = self._acao_dimensoes['estado_14']        
             
    def _estado_final(self):
        self._reforco_imediato = self._estados_reforcos['estado_final']
        self.reforco += self._reforco_imediato
        self._finalizado = self._estados_finalizado['estado_final']
        self._estado_texto = self._estados_texto['estado_final']
        print("\tReforço acumulado de {0}".format(self.reforco))
        self._estado_acao = ""
        
    def _pacote_acoes(self):
        if self._valor_estado in [1, 4, 7, 8, 10, 11, 13]:
            return [0]
        elif self._valor_estado in [2]: 
            return [0, 1, 2]
        elif self._valor_estado in [3, 5, 12]:
            return [0, 1]
        elif self._valor_estado in [9, 6]:
            return [0, 1, 2, 3]
        
    def checa_acao(self, acao):
        if acao in self._pacote_acoes():
            return True
        else:
            return False
    
    def read_1(self):
        return self._estado_texto, self._estado_acao, self._espaco_acoes, self._reforco_imediato, self._finalizado

    def read(self):
        return self._estado_texto, self._estado_acao, self._espaco_acoes

    def imprimeAcao(self, acoes):
        for cont, acao in enumerate(acoes):
            print("\t[{0}] {1}".format(cont, acao))

    def emulador(self, acao):
        if self._valor_estado == 2 and acao == 0: # ok
            return self._estados_texto['estado_6'], self._acao_textos['estado_6'], self._acao_dimensoes['estado_6'], self._estados_reforcos['estado_6'], self._estados_finalizado['estado_1']
        elif self._valor_estado == 2 and acao == 1: # ok
            return self._estados_texto['estado_9'], self._acao_textos['estado_9'], self._acao_dimensoes['estado_9'], self._estados_reforcos['estado_9'], self._estados_finalizado['estado_1']
        elif self._valor_estado in [1, 3, 4] and acao == 0:
            return self._estados_texto['estado_2'], self._acao_textos['estado_2'], self._acao_dimensoes['estado_2'], self._estados_reforcos['estado_2'], self._estados_finalizado['estado_1']
        elif self._valor_estado == 3 and acao == 1:
            return self._estados_texto['estado_5'], self._acao_textos['estado_5'], self._acao_dimensoes['estado_5'], self._estados_reforcos['estado_5'], self._estados_finalizado['estado_1']
        elif self._valor_estado == 2 and acao == 2: # ok
            return self._estados_texto['estado_4'], self._acao_textos['estado_4'], self._acao_dimensoes['estado_4'], self._estados_reforcos['estado_4'], self._estados_finalizado['estado_1']
        elif self._valor_estado == 5 and acao == 1:
            return self._estados_texto['estado_9'], self._acao_textos['estado_9'], self._acao_dimensoes['estado_9'], self._estados_reforcos['estado_9'], self._estados_finalizado['estado_1']
        elif self._valor_estado == 6 and acao == 1:
            return self._estados_texto['estado_7'], self._acao_textos['estado_7'], self._acao_dimensoes['estado_7'], self._estados_reforcos['estado_7'], self._estados_finalizado['estado_1']
        elif self._valor_estado in [7, 8] and acao == 0:
            return self._estados_texto['estado_6'], self._acao_textos['estado_6'], self._acao_dimensoes['estado_6'], self._estados_reforcos['estado_6'], self._estados_finalizado['estado_1']
        elif self._valor_estado == 6 and acao == 2:
            return self._estados_texto['estado_8'], self._acao_textos['estado_7'], self._acao_dimensoes['estado_7'], self._estados_reforcos['estado_7'], self._estados_finalizado['estado_1']
        elif self._valor_estado == 9 and acao == 1:
            return self._estados_texto['estado_10'], self._acao_textos['estado_10'], self._acao_dimensoes['estado_10'], self._estados_reforcos['estado_10'], self._estados_finalizado['estado_1']
        elif self._valor_estado in [6, 10, 11] and acao == 0:
            return self._estados_texto['estado_9'], self._acao_textos['estado_9'], self._acao_dimensoes['estado_9'], self._estados_reforcos['estado_9'], self._estados_finalizado['estado_1']
        elif self._valor_estado == 9 and acao == 2:
            return self._estados_texto['estado_11'], self._acao_textos['estado_10'], self._acao_dimensoes['estado_10'], self._estados_reforcos['estado_10'], self._estados_finalizado['estado_1']
        elif self._valor_estado in [5, 9, 13] and acao == 0:
            return self._estados_texto['estado_12'], self._acao_textos['estado_12'], self._acao_dimensoes['estado_12'], self._estados_reforcos['estado_12'], self._estados_finalizado['estado_1']
        elif self._valor_estado == 12 and acao == 0:
            return self._estados_texto['estado_13'], self._acao_textos['estado_13'], self._acao_dimensoes['estado_13'], self._estados_reforcos['estado_13'], self._estados_finalizado['estado_1']
        elif self._valor_estado == 12 and acao == 1:
            return self._estados_texto['estado_final'], self._acao_textos['estado_final'], self._acao_dimensoes['estado_final'], self._estados_reforcos['estado_final'], self._estados_finalizado['estado_final']
        elif self._valor_estado == 9 and acao == 3:
            return self._estados_texto['estado_6'], self._acao_textos['estado_6'], self._acao_dimensoes['estado_6'], self._estados_reforcos['estado_6'], self._estados_finalizado['estado_1']
        elif self._valor_estado == 6 and acao == 3:
            return self._estados_texto['estado_2'], self._acao_textos['estado_2'], self._acao_dimensoes['estado_2'], self._estados_reforcos['estado_2'], self._estados_finalizado['estado_1']
            
        
if __name__ == '__main__':
    AMN = AdmiravelMundoNovo()
    estado, acao, dimensao_acao, reforco_imediato, finalizado = AMN.read_1()
    print("\tReforço: {0}".format(reforco_imediato))
    print(estado)
    AMN.imprimeAcao(acao)
    while not finalizado:
        acao_atual = int(input("\t>>> "))
        if AMN.checa_acao(acao_atual):
            pass
        else:
            while not AMN.checa_acao(acao_atual):
                print("\tAção não reconhecida com o contexto do jogo.")
                acao_atual = int(input("\t>>> "))
        print()
        AMN.transicao_estado(acao_atual)
        estado, acao, dimensao_acao, reforco_imediato, finalizado = AMN.read_1()
        print("\tReforço: {0}".format(reforco_imediato))
        print(estado)
        AMN.imprimeAcao(acao)
    print("\tReforço acumulado de {0}".format(AMN.reforco))
