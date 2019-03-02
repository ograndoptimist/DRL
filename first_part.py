"""
    \tSeja bem-vindo ao Admirável Mundo Novo!
    \tO objetivo do jogo é dar suporte ao desenvolvimento de Agentes Inteligentes que utilizam Deep Reinforcement Learning
    \tpara tarefas de Processamento de Linguagem Natural em língua portuguesa.        
"""

print(__doc__)

class AdmiravelMundoNovo(object):
    def __init__(self):
        self.estado_inicial()
        self.reforco = 0
        self.checa_estado = False

    def transicao_estado(self, acao):
        if self.valor_estado == 1 and acao == 0:
            self.estado_1()

        elif self.valor_estado == 2 and acao == 0:
            self.estado_2()
        elif self.valor_estado == 2 and acao == 1:
            self.estado_leste()
        elif self.valor_estado == 2.25 and acao == 0:
            self.estado_1()
        elif self.valor_estado == 2.25 and acao == 1:
            self.estado_passagem_secreta()
        elif self.valor_estado == 2 and acao == 2:
            self.estado_oeste()
        elif self.valor_estado == 2.5 and acao == 0:
            self.estado_1()
        elif self.valor_estado == 2.75 and acao == 0:
            self.estado_4()
        elif self.valor_estado == 2.75 and acao == 1:
            self.estado_leste()

        elif self.valor_estado == 3 and acao == 1:
            self.estado_2_esquerda()
        elif self.valor_estado == 3.25 and acao == 0:
            self.estado_2()
        elif self.valor_estado == 3.5 and acao == 0:
            self.estado_2()
        elif self.valor_estado == 3 and acao == 2:
            self.estado_2_direita()
        elif self.valor_estado == 3 and acao == 0:
            self.estado_3()

        elif self.valor_estado == 4 and acao == 1:
            self.estado_3_esquerda()
        elif self.valor_estado == 4.25 and acao == 0:
            self.estado_3()
        elif self.valor_estado == 4.5 and acao == 0:
            self.estado_3()
        elif self.valor_estado == 4 and acao == 2:
            self.estado_3_direita()
        elif self.valor_estado == 4 and acao == 0:
            self.estado_4()

        elif self.valor_estado == 5 and acao == 0:
            self.estado_4_esquerda()
        elif self.valor_estado == 5.5 and acao == 0:
            self.estado_4()
        elif self.valor_estado == 5 and acao == 1:
            self.estado_final()            

    def estado_inicial(self):
        print()
        print("\tPrimeiro Desafio")
        print("\tReforço: 0")
        print("\tVocê está na entrada da ilha da Fantasia. O objetivo do jogo é coletar a chave preciosa de ouro.\n\tPara tal, você precisa vasculhar os andares do Castelo Principal. Logo a sua frente há uma ponte\n\tque dá acesso à entrada do Castelo principal. ")
        print("\t[0] Atravesse a ponte.")
        self.valor_estado = 1

    def estado_1(self):
        self.reforco += 1
        print()
        print("\tEntrada do Castelo.")
        print("\tReforço: 1")
        print("\tAgora você está na porta principal do Castelo. O Castelo possui 3 andares que você pode explorar\n\tatravés de belíssimas escadas. Em um desses três andares, está o tesouro que procuras...")
        print("\t[0] Abra a porta.")
        print("\t[1] Vá para o leste.")
        print("\t[2] Vá para o oeste.")
        self.valor_estado = 2

    def estado_leste(self):
        self.reforco += 1
        print()
        print("\tJardim do Castelo")
        print("\tReforço: 1")
        print("\tNo Jardim do Castelo você tem acesso as mais belas plantas de todo o reino. Aqui temos flores, maçãs....e quem sabe uma\n\tpassagem secreta até o tesouro mais procurado nestes tempos....")
        print("\t[0] Volte para a entrada do Castelo.")
        print("\t[1] Vá para a passagem secreta.")
        self.valor_estado = 2.25

    def estado_oeste(self):
        print()
        print("\tMosteiro dos Bravos Cavalos")
        print("\tReforço: 0")
        print("\tVocê pode aproveitar que chegou até aqui e ajudar o zelador a manter os cavalos com os mais belos cortes de crina.\n\tNo entanto, tomaria cuidado para não toma nenhum coice, já que aqui também se\n\tencontram os cavalos mais selvagens do Reino da Ilha da Fantasia...")
        print("\t[0] Volte para a entrada do Castelo.")
        self.valor_estado = 2.5

    def estado_passagem_secreta(self):
        self.reforco += 10
        print()
        print("\tA passagem secreta")
        print("\tReforço: 10")
        print("\tDaqui em diante, o teletransporte do castelo se encarrega do trabalho de te aproximar do tesouro que procuras.\n\tTalvez o melhor seja sempre seguir em frente, já que a vida imita a arte...\n\tmas a escolha está em suas mãos...")
        print("\t[0] Seguir em frente.")
        print("\t[1] Voltar para o jardim.")
        self.valor_estado = 2.75

    def estado_2(self):
        self.reforco += 1
        print()
        print("\tSalão Principal")
        print("\tReforço: 1")
        print("\tBem-vindo ao Salão Principal do Castelo. Nosso Castelo está sempre recebendo as mais belas\n\tdivindades do Reino da Fantasia. O tapete vermelho pode te levar ao salão de jantar se você seguir\n\tà esquerda, ou caso contrário, à direita, você alcança a biblioteca dos mais sábios livros que\n\ttalvez esconda os segredos mais esperados de todo o novo continente.\n\tTambém há a possibilidade de subir as escadas para se chegar ao próximo andar.")
        print("\t[0] Suba as escadas.")
        print("\t[1] Siga à esquerda.")
        print("\t[2] Siga à direita.")
        self.valor_estado = 3

    def estado_2_esquerda(self):
        print()
        print("\tSalão de Jantar")
        print("\tReforço: 0")
        print("\tOs mais belos jantares são servidos à nobreza do Reino neste local. Somente os de sangue mais\n\tpuro podem utilizar da louça sobre a mesa. O antigo dono da chave preciosa já esteve por aqui.")
        print("\t[0] Volte ao salão principal.")
        self.valor_estado = 3.25

    def estado_2_direita(self):
        print()
        print("\tBiblioteca dos Mais Sábios")
        print("\tReforço: 0")
        print("\tPor esta biblioteca já passaram os mais sábios do Reino. Mentes brilhantes produziram obras\n\tque ficarão por aqui por toda a eternidade. Talvez se você ler todos os livros, será capaz de\n\tencontrar a reposta do enigma do paradeiro da chave preciosa de ouro.")
        print("\t[0] Volte ao salão principal.")
        self.valor_estado = 3.5

    def estado_3(self):
        self.reforco += 1
        print()
        print("\tSegundo andar")
        print("\tReforço: 1")
        print("\tVocê conseguiu subir as longas escadas do Castelo Principal e chegar ao andar de travessuras.\n\tEste andar é geralmente povoado pelos bobos da corte, então é melhor ficar atento para evitar\n\tapuros com os mais astutos do povoado.")
        print("\t[0] Suba as escadas.")
        print("\t[1] Siga à esquerda.")
        print("\t[2] Siga à direita.")
        self.valor_estado = 4

    def estado_3_esquerda(self):
        print()
        print("\tTreinamento dos Travessos")
        print("\tReforço: 0")
        print("\tCuidado para não atrapalha-los. Aqui eles preparam as melhores perfomances para toda a corte. ")
        print("\t[0] Volte ao salão principal.")
        self.valor_estado = 4.25

    def estado_3_direita(self):
        print()
        print("\tDormitório dos Travessos")
        print("\tReforço: 0")
        print("\tAté nos sonhos os bobos da corte aprontam as mais astutas travessuras. Se eu fosse você tomaria\n\tcuidado para não acordá-los, ou é melhor se preparar para se tornar o palhaço da corte...")
        print("\t[0] Volte ao salão principal.")
        self.valor_estado = 4.5

    def estado_4(self):
        self.reforco += 1
        print()
        print("\tSantuário dos sonhos esquecidos")
        print("\tReforço: 1")
        print("\tOs sonhos mais profundos viajam pelos quartos deste andar. Aqui o inconsciente se comunica com o\n\tconsciente dos seres do Reino. Dizem por aí que sonharam que a chave estaria por aqui, mas\n\tcabe a você verificar quarto por quarto se é uma verdade ou apenas mais um dos sonhos.")
        print("\t[0] Siga à esquerda.")
        print("\t[1] Siga à direita.")
        self.valor_estado = 5

    def estado_4_esquerda(self):
        self.reforco -= 10
        print()
        print("\tO esquecimento profundo")
        print("\tReforço: -10")
        print("\tEste quarto traz o esquecimento temporário a quem nele adentra. Infelizmente, para aqueles que \n\taqui tem acesso acabam sendo teletransportados para o salão principal do primeiro andar.")
        self.valor_estado = 5.5
        self.estado_2()

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
            return [0]
        elif self.valor_estado in [2, 2.25, 2.5, 2.75]:
            return [0, 1, 2]
        elif self.valor_estado in [3, 3.25, 3.5]:
            return [0, 1, 2, 3]
        elif self.valor_estado in [4, 4.25, 4.5]:
            return [0, 1, 2, 3]
        elif self.valor_estado in [5, 5.5]:
            return [0, 1]

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
        acao = int(input("\t>>> "))
        while jogo.checa_acao(acao):
            print("\tAção não reconhecida com o contexto do jogo.")
            acao = int(input("\t>>> "))
        jogo.transicao_estado(acao)
