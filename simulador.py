"""
    \tSeja bem-vindo ao Admirável Mundo Novo!
    \tO objetivo do jogo é dar suporte ao desenvolvimento de Agentes Inteligentes que utilizam Deep Reinforcement Learning
    \tpara tarefas de Processamento de Linguagem Natural em língua portuguesa.
    \tAutor: Gabriel Pontes (@ograndoptimist)       
"""

from textos import ESTADOS, ACOES, REFORCOS, FINALIZADO, DIMENSOES

print(__doc__)

class AdmiravelMundoNovo(object):
    def __init__(self):
        self.reforco = 0
        self.checa_estado = False
        self.estado_texto = None
        self.estado_acao = None
        self.finalizado = False
        self.espaco_acoes = 0
        self.estados_texto = ESTADOS
        self.acao_textos =  ACOES
        self.acao_dimensoes = DIMENSOES
        self.estados_reforcos = REFORCOS
        self.estados_finalizado = FINALIZADO

        self.estado_inicial()

    def transicao_estado(self, acao):        
        if self.valor_estado == 2 and acao == 0:
            self.estado_2()
        elif self.valor_estado == 2 and acao == 1:
            self.estado_leste()
        elif self.valor_estado in [1, 2.25, 2.5] and acao == 0:
            self.estado_1()
        elif self.valor_estado == 2.25 and acao == 1:
            self.estado_passagem_secreta()
        elif self.valor_estado == 2 and acao == 2:
            self.estado_oeste()
        elif self.valor_estado == 2.75 and acao == 1:
            self.estado_leste()
        elif self.valor_estado == 3 and acao == 1:
            self.estado_2_esquerda()
        elif self.valor_estado in [3.25, 3.5] and acao == 0:
            self.estado_2()
        elif self.valor_estado == 3 and acao == 2:
            self.estado_2_direita()        
        elif self.valor_estado == 4 and acao == 1:
            self.estado_3_esquerda()
        elif self.valor_estado in [3, 4.25, 4.5] and acao == 0:
            self.estado_3()
        elif self.valor_estado == 4 and acao == 2:
            self.estado_3_direita()
        elif self.valor_estado in [2.75, 4] and acao == 0:
            self.estado_4()
        elif self.valor_estado == 5 and acao == 0:
            self.estado_4_esquerda()
        elif self.valor_estado == 5 and acao == 1:
            self.estado_final()
        elif self.valor_estado == 5.25 and acao == 0:
            self.estado_4()

    def estado_inicial(self):
        self.reforco_imediato = self.estados_reforcos['estado_inicial']
        self.reforco += self.reforco_imediato
        self.valor_estado = 1
        self.finalizado = self.estados_finalizado['estado_inicial']
        self.estado_texto = self.estados_texto['estado_inicial']
        self.estado_acao = self.acao_textos['estado_inicial']
        self.espaco_acoes = self.acao_dimensoes['estado_inicial']
                
    def estado_1(self):
        self.reforco_imediato = self.estados_reforcos['estado_1']
        self.reforco += self.reforco_imediato
        self.valor_estado = 2
        self.finalizado = self.estados_finalizado['estado_inicial']
        self.estado_texto = self.estados_texto['estado_1']
        self.estado_acao = self.acao_textos['estado_1']
        self.espaco_acoes = self.acao_dimensoes['estado_1']
        
    def estado_leste(self):
        self.reforco_imediato = self.estados_reforcos['estado_leste']
        self.reforco += self.reforco_imediato
        self.valor_estado = 2.25
        self.finalizado = self.estados_finalizado['estado_inicial']
        self.estado_texto = self.estados_texto['estado_leste']
        self.estado_acao = self.acao_textos['estado_leste']
        self.espaco_acoes = self.acao_dimensoes['estado_leste']
        
    def estado_oeste(self):
        self.reforco_imediato = self.estados_reforcos['estado_oeste']
        self.reforco += self.reforco_imediato
        self.valor_estado = 2.5
        self.finalizado = self.estados_finalizado['estado_inicial']
        self.estado_texto = self.estados_texto['estado_oeste']
        self.estado_acao = self.acao_textos['estado_oeste']
        self.espaco_acoes = self.acao_dimensoes['estado_oeste']
        
    def estado_passagem_secreta(self):
        self.reforco_imediato = self.estados_reforcos['estado_passagem_secreta']
        self.reforco += self.reforco_imediato
        self.valor_estado = 2.75
        self.finalizado = self.estados_finalizado['estado_inicial']
        #print("\tReforço: 10")
        self.estado_texto = self.estados_texto['estado_passagem_secreta']
        self.estado_acao = self.acao_textos['estado_passagem_secreta']
        self.espaco_acoes = self.acao_dimensoes['estado_passagem_secreta']
        
    def estado_2(self):
        self.reforco_imediato = self.estados_reforcos['estado_2']
        self.reforco += self.reforco_imediato
        self.valor_estado = 3
        self.finalizado = self.estados_finalizado['estado_inicial']
        self.estado_texto = self.estados_texto['estado_2']
        self.estado_acao = self.acao_textos['estado_2']
        self.espaco_acoes = self.acao_dimensoes['estado_2']
        
    def estado_2_esquerda(self):
        self.reforco_imediato = self.estados_reforcos['estado_2_esquerda_direita']
        self.reforco += self.reforco_imediato
        self.valor_estado = 3.25
        self.finalizado = self.estados_finalizado['estado_inicial']
        self.estado_texto = self.estados_texto['estado_2_esquerda']
        self.estado_acao = self.acao_textos['estado_2_esquerda_direita']
        self.espaco_acoes = self.acao_dimensoes['estado_2_esquerda_direita']
        
    def estado_2_direita(self):
        self.reforco_imediato = self.estados_reforcos['estado_2_esquerda_direita']
        self.reforco += self.reforco_imediato
        self.valor_estado = 3.5
        self.finalizado = self.estados_finalizado['estado_inicial']
        self.estado_texto = self.estados_texto['estado_2_direita']
        self.estado_acao = self.acao_textos['estado_2_esquerda_direita']
        self.espaco_acoes = self.acao_dimensoes['estado_2_esquerda_direita']
        
    def estado_3(self):
        self.reforco_imediato = self.estados_reforcos['estado_3']
        self.reforco += self.reforco_imediato
        self.valor_estado = 4
        self.finalizado = self.estados_finalizado['estado_inicial']
        self.estado_texto = self.estados_texto['estado_3']
        self.estado_acao = self.acao_textos['estado_3']
        self.espaco_acoes = self.acao_dimensoes['estado_3']
        
    def estado_3_esquerda(self):
        self.reforco_imediato = self.estados_reforcos['estado_3_esquerda_direita']
        self.reforco += self.reforco_imediato
        self.valor_estado = 4.25
        self.finalizado = self.estados_finalizado['estado_inicial']
        self.estado_texto = self.estados_texto['estado_3_esquerda']
        self.estado_acao = self.acao_textos['estado_3_esquerda_direita']
        self.espaco_acoes = self.acao_dimensoes['estado_3_esquerda_direita']
        
    def estado_3_direita(self):
        self.reforco_imediato = self.estados_reforcos['estado_3_esquerda_direita']
        self.reforco += self.reforco_imediato
        self.valor_estado = 4.5
        self.finalizado = self.estados_finalizado['estado_inicial']
        self.estado_texto = self.estados_texto['estado_3_direita']
        self.estado_acao = self.acao_textos['estado_3_esquerda_direita']
        self.espaco_acoes = self.acao_dimensoes['estado_3_esquerda_direita']
        
    def estado_4(self):
        self.reforco_imediato = self.estados_reforcos['estado_4']
        self.reforco += self.reforco_imediato
        self.valor_estado = 5
        self.finalizado = self.estados_finalizado['estado_inicial']
        self.estado_texto = self.estados_texto['estado_4']
        self.estado_acao = self.acao_textos['estado_4']
        self.espaco_acoes = self.acao_dimensoes['estado_4']
        
    def estado_4_esquerda(self):
        self.reforco_imediato = self.estados_reforcos['estado_4_esquerda']
        self.reforco -= self.reforco_imediato
        self.valor_estado = 5.25
        self.finalizado = self.estados_finalizado['estado_inicial']
        self.finalizado = self.estados_finalizado['estado_inicial']
        self.estado_texto = self.estados_texto['estado_4_esquerda']
        self.estado_acao = self.acao_textos['estado_4_esquerda']
        self.espaco_acoes = self.acao_dimensoes['estado_4_esquerda']
             
    def estado_final(self):
        self.reforco_imediato = self.estados_reforcos['estado_final']
        self.reforco += self.reforco_imediato
        self.finalizado = self.estados_finalizado['estado_final']
        self.estado_texto = self.estados_texto['estado_final']
        print("\tReforço acumulado de {0}".format(self.reforco))
        self.estado_acao = ""
        
    def pacote_acoes(self):
        if self.valor_estado in [1, 2.5, 3.25, 3.5, 4.25, 4.5, 5.25]:
            return [0]
        elif self.valor_estado in [2, 3, 4]: 
            return [0, 1, 2]
        elif self.valor_estado in [2.25, 2.75, 5]:
            return [0, 1]        
        
    def checa_acao(self, acao):
        if acao in self.pacote_acoes():
            return True
        else:
            return False
    
    def read_1(self):
        return self.estado_texto, self.estado_acao, self.espaco_acoes, self.reforco_imediato, self.finalizado

    def read(self):
        return self.estado_texto, self.estado_acao, self.espaco_acoes

    def imprimeAcao(self, acoes):
        for cont, acao in enumerate(acoes):
            print("\t[{0}] {1}".format(cont, acao))

    def emulador(self, acao):
        if self.valor_estado == 2 and acao == 0:
            return self.estados_texto['estado_2'], self.acao_textos['estado_2'], self.acao_dimensoes['estado_2'], self.estados_reforcos['estado_2'], self.estados_finalizado['estado_inicial']
        elif self.valor_estado == 2 and acao == 1:
            return self.estados_texto['estado_leste'], self.acao_textos['estado_leste'], self.acao_dimensoes['estado_leste'], self.estados_reforcos['estado_leste'], self.estados_finalizado['estado_inicial']
        elif self.valor_estado in [1, 2.25, 2.5] and acao == 0:
            return self.estados_texto['estado_1'], self.acao_textos['estado_1'], self.acao_dimensoes['estado_1'], self.estados_reforcos['estado_1'], self.estados_finalizado['estado_inicial']
        elif self.valor_estado == 2.25 and acao == 1:
            return self.estados_texto['estado_passagem_secreta'], self.acao_textos['estado_passagem_secreta'], self.acao_dimensoes['estado_passagem_secreta'], self.estados_reforcos['estado_passagem_secreta'], self.estados_finalizado['estado_inicial']
        elif self.valor_estado == 2 and acao == 2:
            return self.estados_texto['estado_oeste'], self.acao_textos['estado_oeste'], self.acao_dimensoes['estado_oeste'], self.estados_reforcos['estado_oeste'], self.estados_finalizado['estado_inicial']
        elif self.valor_estado == 2.75 and acao == 1:
            return self.estados_texto['estado_leste'], self.acao_textos['estado_leste'], self.acao_dimensoes['estado_leste'], self.estados_reforcos['estado_leste'], self.estados_finalizado['estado_inicial']
        elif self.valor_estado == 3 and acao == 1:
            return self.estados_texto['estado_2_esquerda'], self.acao_textos['estado_2_esquerda_direita'], self.acao_dimensoes['estado_2_esquerda_direita'], self.estados_reforcos['estado_2_esquerda_direita'], self.estados_finalizado['estado_inicial']
        elif self.valor_estado in [3.25, 3.5] and acao == 0:
            return self.estados_texto['estado_2'], self.acao_textos['estado_2'], self.acao_dimensoes['estado_2'], self.estados_reforcos['estado_2'], self.estados_finalizado['estado_inicial']
        elif self.valor_estado == 3 and acao == 2:
            return self.estados_texto['estado_2_direita'], self.acao_textos['estado_2_esquerda_direita'], self.acao_dimensoes['estado_2_esquerda_direita'], self.estados_reforcos['estado_2_esquerda_direita'], self.estados_finalizado['estado_inicial']
        elif self.valor_estado == 4 and acao == 1:
            return self.estados_texto['estado_3_esquerda'], self.acao_textos['estado_3_esquerda_direita'], self.acao_dimensoes['estado_3_esquerda_direita'], self.estados_reforcos['estado_3_esquerda_direita'], self.estados_finalizado['estado_inicial']
        elif self.valor_estado in [3, 4.25, 4.5] and acao == 0:
            return self.estados_texto['estado_3'], self.acao_textos['estado_3'], self.acao_dimensoes['estado_3'], self.estados_reforcos['estado_3'], self.estados_finalizado['estado_inicial']
        elif self.valor_estado == 4 and acao == 2:
            return self.estados_texto['estado_3_direita'], self.acao_textos['estado_3_esquerda_direita'], self.acao_dimensoes['estado_3_esquerda_direita'], self.estados_reforcos['estado_3_esquerda_direita'], self.estados_finalizado['estado_inicial']
        elif self.valor_estado in [2.75, 4] and acao == 0:
            return self.estados_texto['estado_4'], self.acao_textos['estado_4'], self.acao_dimensoes['estado_4'], self.estados_reforcos['estado_4'], self.estados_finalizado['estado_inicial']
        elif self.valor_estado == 5 and acao == 0:
            return self.estados_texto['estado_4_esquerda'], self.acao_textos['estado_4_esquerda'], self.acao_dimensoes['estado_4_esquerda'], self.estados_reforcos['estado_4_esquerda'], self.estados_finalizado['estado_inicial']
        elif self.valor_estado == 5 and acao == 1:
            return self.estados_texto['estado_final'], self.acao_textos['estado_final'], self.acao_dimensoes['estado_final'], self.estados_reforcos['estado_final'], self.estados_finalizado['estado_final']
        elif self.valor_estado == 5.25 and acao == 0:
            return self.estados_texto['estado_4'], self.acao_textos['estado_4'], self.acao_dimensoes['estado_4'], self.estados_reforcos['estado_4'], self.estados_finalizado['estado_inicial']

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
