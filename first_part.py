"""
    \tSeja bem-vindo ao Admirável Mundo Novo!
    \tO objetivo do jogo é dar suporte ao desenvolvimento de Agentes Inteligentes utilizando-se de Deep Reinforcement Learning
    \tpara tarefas de Processamento de Linguagem Natural em língua portuguesa.        
"""

print(__doc__)


class AdmiravelMundoNovo(object):
    def __init__(self):
        self.estado_inicial()
        self.reforco = 0
        self.checa_estado = False

    def transicao_estado(self, acao):
        if self.valor_estado == 1 and acao == 'atravessa ponte':
            self.estado_1()

        elif self.valor_estado == 2 and acao == 'abra a porta':
            self.estado_2()

        elif self.valor_estado == 3 and acao == 'siga à esquerda':
            self.estado_2_esquerda()
        elif self.valor_estado == 3.25 and acao == 'volte ao salão principal':
            self.estado_2()
        elif self.valor_estado == 3.5 and acao == 'volte ao salão principal':
            self.estado_2()
        elif self.valor_estado == 3 and acao == 'siga à direita':
            self.estado_2_direita()
        elif self.valor_estado == 3 and acao == 'suba as escadas':
            self.estado_3()

        elif self.valor_estado == 4 and acao == 'siga à esquerda':
            self.estado_3_esquerda()
        elif self.valor_estado == 4.25 and acao == 'volte ao salão principal':
            self.estado_3()
        elif self.valor_estado == 4.5 and acao == 'volte ao salão principal':
            self.estado_3()
        elif self.valor_estado == 4 and acao == 'siga à direita':
            self.estado_3_direita()
        elif self.valor_estado == 4 and acao == 'suba as escadas':
            self.estado_4()
            

    def estado_inicial(self):
        print()
        print("\tPrimeiro Desafio")
        print("\tReforço: 0")
        print("\tVocê está na entrada da ilha da Fantasia. O objetivo do jogo é coletar a chave preciosa de ouro.\n\tPara tal, você precisa vasculhar os andares do Castelo Principal. Logo a sua frente há uma ponte\n\tque dá acesso à entrada do Castelo principal. ")
        self.valor_estado = 1

    def estado_1(self):
        self.reforco += 1
        print()
        print("\tEntrada do Castelo.")
        print("\tReforço: 1")
        print("\tAgora você está na porta principal do Castelo. O Castelo possui 3 andares que você pode explorar\n\tatravés de belíssimas escadas. Em um desses três andares, está o tesouro que procuras...")
        self.valor_estado = 2

    def estado_2(self):
        self.reforco += 1
        print()
        print("\tSalão Principal")
        print("\tReforço: 1")
        print("\tBem-vindo ao Salão Principal do Castelo. Nosso Castelo está sempre recebendo as mais belas\n\tdivindades do Reino da Fantasia. O tapete vermelho pode te levar ao salão de jantar se você seguir\n\tà esquerda, ou caso contrário, à direita, você alcança a biblioteca dos mais sábios livros que\n\ttalvez esconda os segredos mais esperados de todo o novo continente.\n\tTambém há a possibilidade de subir as escadas para se chegar ao próximo andar.")
        self.valor_estado = 3

    def estado_2_esquerda(self):
        self.reforco += 0
        print()
        print("\tSalão de Jantar")
        print("\tReforço: 0")
        print("\tOs mais belos jantares são servidos à nobreza do Reino neste local. Somente os de sangue mais\n\tpuro podem utilizar da louça sobre a mesa. O antigo dono da chave preciosa já esteve por aqui.")
        self.valor_estado = 3.25

    def estado_2_direita(self):
        self.reforco += 0
        print()
        print("\tBiblioteca dos Mais Sábios")
        print("\tReforço: 0")
        print("\tPor esta biblioteca já passaram os mais sábios do Reino. Mentes brilhantes produziram obras\n\tque ficarão por aqui por toda a eternidade. Talvez se você ler todos os livros, será capaz de\n\tencontrar a reposta do enigma do paradeiro da chave preciosa de ouro.")
        self.valor_estado = 3.5

    def estado_3(self):
        self.reforco += 1
        print()
        print("\tSegundo andar")
        print("\tReforço: 1")
        print("\tVocê conseguiu subir as longas escadas do Castelo Principal e chegar ao andar de travessuras.\n\tEste andar é geralmente povoado pelos bobos da corte, então é melhor ficar atento para evitar\n\tapuros com os mais astutos do povoado.")
        self.valor_estado = 4

    def estado_3_esquerda(self):
        self.reforco += 0
        print()
        print("\tQuarto do Treinamento dos Travessos")
        print("\tReforço: 0")
        print("\t")
        self.valor_estado = 4.25

    def estado_3_direita(self):
        self.reforco += 0
        print()
        print("\tQuarto do Dormitório dos Travessos")
        print("\tReforço: 0")
        print("\t")
        self.valor_estado = 4.5

    def estado_4(self):
        self.reforco += 1
        print()
        print("\tQuarto de Treinamento dos Travessos")
        print("\tReforço: 0")
        print("\t")
        self.valor_estado = 5

    def estado_final(self):
        self.reforco += 100
        print()
        print("\tFinal do jogo.")
        print("\tReforço: 100")
        print("\tParabéns! Você conseguiu coletar a chave de ouro preciosa! Sendo assim, o jogo está finalizado! ")
        print("\tReforço acumulado de {0}".format(self.reforco))
        self.checa_estado = True

    def pacote_acoes(self):
        if self.valor_estado == 1:
            return ['atravessa ponte']
        elif self.valor_estado == 2:
            return ['abra a porta']
        elif self.valor_estado in [3, 3.25, 3.5]:
            return ['siga à esquerda', 'suba as escadas', 'siga à direita', 'volte ao salão principal']
        elif self.valor_estado in [4, 4.25, 4.5]:
            return ['siga à esquerda', 'suba as escadas', 'siga à direita', 'volte ao salão principal']

    def checa_acao(self, acao):
        if acao not in self.pacote_acoes():
            return True
        else:
            return False

    def checa_fim(self):
        if not self.checa_estado:
            return True
        else:
            return False


if __name__ == '__main__':
    jogo = AdmiravelMundoNovo()
    while jogo.checa_fim():
        acao = input("\t>>> ")
        while jogo.checa_acao(acao):
            print("\tAção não reconhecida com o contexto do jogo.")
            acao = input("\t>>> ")
        jogo.transicao_estado(acao)
