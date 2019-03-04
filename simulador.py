"""
    \tSeja bem-vindo ao Admirável Mundo Novo!
    \tO objetivo do jogo é dar suporte ao desenvolvimento de Agentes Inteligentes que utilizam Deep Reinforcement Learning
    \tpara tarefas de Processamento de Linguagem Natural em língua portuguesa.
    \tAutor: Gabriel Pontes (@ograndoptimist)       Mentora: Karla Figueiredo
"""

print(__doc__)

class AdmiravelMundoNovo(object):
    def __init__(self):
        self.reforco = 0
        self.checa_estado = False
        self.estado_texto = ""
        self.estado_acao = ""
        self.finalizado = False
        self.espaco_acoes = 0

        self.estado_inicial()

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
        elif self.valor_estado == 5 and acao == 1:
            self.estado_final()            

    def estado_inicial(self):
        reforco_imediato = 0
        self.reforco += reforco_imediato
        self.valor_estado = 1
        self.finalizado = False
        print("\tReforço: 0")
        self.estado_texto = "\tPrimeiro desafio\n\tVocê está na entrada da ilha da Fantasia. O objetivo do jogo é coletar a chave preciosa de ouro.\n\tPara tal, você precisa vasculhar os andares do Castelo Principal. Logo a sua frente há uma ponte\n\tque dá acesso à entrada do Castelo principal."
        self.estado_acao = ["[0] Atravesse a ponte."]
        self.espaco_acoes = len(self.estado_acao)
        return reforco_imediato, self.estado_texto, self.estado_acao

    def estado_1(self):
        reforco_imediato = 1
        self.reforco += reforco_imediato
        self.valor_estado = 2
        self.finalizado = False
        print("\tReforço: 1")
        self.estado_texto = "\tEntrada do Castelo.\n\tAgora você está na porta principal do Castelo. O Castelo possui 3 andares que você pode explorar\n\tatravés de belíssimas escadas. Em um desses três andares, está o tesouro que procuras..."
        self.estado_acao = ["[0] Abra a porta.", "[1] Vá para o leste.", "[2] Vá para o oeste."]
        self.espaco_acoes = len(self.estado_acao)
        return reforco_imediato, self.estado_texto, self.estado_acao

    def estado_leste(self):
        reforco_imediato = 1
        self.reforco += reforco_imediato
        self.valor_estado = 2.25
        self.finalizado = False
        print("\tReforço: 1")
        self.estado_texto = "\tJardim do Castelo\n\tNo Jardim do Castelo você tem acesso as mais belas plantas de todo o reino. Aqui temos flores, maçãs....e quem sabe uma\n\tpassagem secreta até o tesouro mais procurado nestes tempos...."
        self.estado_acao = ["[0] Volte para a entrada do Castelo.", "[1] Vá para a passagem secreta."]
        self.espaco_acoes = len(self.estado_acao)
        return reforco_imediato, self.estado_texto, self.estado_acao

    def estado_oeste(self):
        reforco_imediato = 0
        self.reforco += reforco_imediato
        self.valor_estado = 2.5
        self.finalizado = False
        print("\tReforço: 0")
        self.estado_texto = "\tMosteiro dos Bravos Cavalos\n\tVocê pode aproveitar que chegou até aqui e ajudar o zelador a manter os cavalos com os mais belos cortes de crina.\n\tNo entanto, tomaria cuidado para não toma nenhum coice, já que aqui também se\n\tencontram os cavalos mais selvagens do Reino da Ilha da Fantasia..."
        self.estado_acao = ["[0] Volte para a entrada do Castelo."]
        self.espaco_acoes = len(self.estado_acao)
        return reforco_imediato, self.estado_texto, self.estado_acao

    def estado_passagem_secreta(self):
        reforco_imediato = 10
        self.reforco += reforco_imediato
        self.valor_estado = 2.75
        self.finalizado = False
        print("\tReforço: 10")
        self.estado_texto = "\tA passagem secreta\n\tDaqui em diante, o teletransporte do castelo se encarrega do trabalho de te aproximar do tesouro que procuras.\n\tTalvez o melhor seja sempre seguir em frente, já que a vida imita a arte...\n\tmas a escolha está em suas mãos..."
        self.estado_acao = ["[0] Seguir em frente.", "[1] Voltar para o jardim."]
        self.espaco_acoes = len(self.estado_acao)
        return reforco_imediato, self.estado_texto, self.estado_acao

    def estado_2(self):
        reforco_imediato = 1
        self.reforco += reforco_imediato
        self.valor_estado = 3
        self.finalizado = False
        print("\tReforço: 1")
        self.estado_texto = "\tSalão Principal\n\tBem-vindo ao Salão Principal do Castelo. Nosso Castelo está sempre recebendo as mais belas\n\tdivindades do Reino da Fantasia. O tapete vermelho pode te levar ao salão de jantar se você seguir\n\tà esquerda, ou caso contrário, à direita, você alcança a biblioteca dos mais sábios livros que\n\ttalvez esconda os segredos mais esperados de todo o novo continente.\n\tTambém há a possibilidade de subir as escadas para se chegar ao próximo andar."
        self.estado_acao = ["[0] Suba as escadas.", "[1] Siga à esquerda.", "[2] Siga à direita."]
        self.espaco_acoes = len(self.estado_acao)
        return reforco_imediato, self.estado_texto, self.estado_acao

    def estado_2_esquerda(self):
        reforco_imediato = 0
        self.reforco += reforco_imediato
        self.valor_estado = 3.25
        self.finalizado = False
        print("\tReforço: 0")
        self.estado_texto = "\tSalão de Jantar\n\tOs mais belos jantares são servidos à nobreza do Reino neste local. Somente os de sangue mais\n\tpuro podem utilizar da louça sobre a mesa. O antigo dono da chave preciosa já esteve por aqui."
        self.estado_acao = ["[0] Volte ao salão principal."]
        self.espaco_acoes = len(self.estado_acao)
        return reforco_imediato, self.estado_texto, self.estado_acao

    def estado_2_direita(self):
        reforco_imediato = 0
        self.reforco += reforco_imediato
        self.valor_estado = 3.5
        self.finalizado = False
        print("\tReforço: 0")        
        self.estado_texto = "\tBiblioteca dos Mais Sábios\n\tPor esta biblioteca já passaram os mais sábios do Reino. Mentes brilhantes produziram obras\n\tque ficarão por aqui por toda a eternidade. Talvez se você ler todos os livros, será capaz de\n\tencontrar a reposta do enigma do paradeiro da chave preciosa de ouro."
        self.estado_acao = ["[0] Volte ao salão principal."]
        self.espaco_acoes = len(self.estado_acao)
        return reforco_imediato, self.estado_texto, self.estado_acao

    def estado_3(self):
        reforco_imediato = 1
        self.reforco += reforco_imediato
        self.valor_estado = 4
        self.finalizado = False
        print("\tReforço: 1")
        self.estado_texto = "\tSegundo andar\n\tVocê conseguiu subir as longas escadas do Castelo Principal e chegar ao andar de travessuras.\n\tEste andar é geralmente povoado pelos bobos da corte, então é melhor ficar atento para evitar\n\tapuros com os mais astutos do povoado."
        self.estado_acao = ["[0] Suba as escadas.", "[1] Siga à esquerda.", "[2] Siga à direita."]
        self.espaco_acoes = len(self.estado_acao)
        return reforco_imediato, self.estado_texto, self.estado_acao

    def estado_3_esquerda(self):
        reforco_imediato = 0
        self.reforco += reforco_imediato
        self.valor_estado = 4.25
        self.finalizado = False
        print("\tReforço: 0")
        self.estado_texto = "\tTreinamento dos Travessos\n\tCuidado para não atrapalha-los. Aqui eles preparam as melhores perfomances para toda a corte."
        self.estado_acao = ["[0] Volte ao salão principal."]
        self.espaco_acoes = len(self.estado_acao)
        return reforco_imediato, self.estado_texto, self.estado_acao

    def estado_3_direita(self):
        reforco_imediato = 0
        self.reforco += reforco_imediato
        self.valor_estado = 4.5
        self.finalizado = False
        print("\tReforço: 0")
        self.estado_texto = "\tDormitório dos Travessos\n\tAté nos sonhos os bobos da corte aprontam as mais astutas travessuras. Se eu fosse você tomaria\n\tcuidado para não acordá-los, ou é melhor se preparar para se tornar o palhaço da corte..."
        self.estado_acao = ["[0] Volte ao salão principal."]
        self.espaco_acoes = len(self.estado_acao)
        return reforco_imediato, self.estado_texto, self.estado_acao

    def estado_4(self):
        reforco_imediato = 1
        self.reforco += reforco_imediato
        self.valor_estado = 5
        self.finalizado = False
        print("\tReforço: 1")
        self.estado_texto = "\tSantuário dos sonhos esquecidos\n\tOs sonhos mais profundos viajam pelos quartos deste andar. Aqui o inconsciente se comunica com o\n\tconsciente dos seres do Reino. Dizem por aí que sonharam que a chave estaria por aqui, mas\n\tcabe a você verificar quarto por quarto se é uma verdade ou apenas mais um dos sonhos."
        self.estado_acao = ["[0] Siga à esquerda.", "[1] Siga à direita."]
        self.espaco_acoes = len(self.estado_acao)
        return reforco_imediato, self.estado_texto, self.estado_acao

    def estado_4_esquerda(self):
        self.reforco -= 10
        print("\tReforço: -10")
        print("\tO esquecimento profundo\n\tEste quarto traz o esquecimento temporário a quem nele adentra. Infelizmente, para aqueles que \n\taqui tem acesso acabam sendo teletransportados para o salão principal do primeiro andar.")
        print()
        self.estado_2()
        
    def estado_final(self):
        reforco_imediato = 100
        self.reforco += reforco_imediato
        self.finalizado = True
        print("\tReforço: 100")
        self.estado_texto = "\tFinal do jogo.\n\tParabéns! Você conseguiu coletar a chave de ouro preciosa! Sendo assim, o jogo está finalizado!"
        print("\tReforço acumulado de {0}".format(self.reforco))
        self.estado_acao = ""
        return reforco_imediato, self.estado_texto, self.estado_acao

    def pacote_acoes(self):
        if self.valor_estado == 1:
            return [0]
        elif self.valor_estado in [2, 2.25, 2.5, 2.75]:
            return [0, 1, 2]
        elif self.valor_estado in [3, 3.25, 3.5]:
            return [0, 1, 2]
        elif self.valor_estado in [4, 4.25, 4.5]:
            return [0, 1, 2]
        elif self.valor_estado in [5, 5.5]:
            return [0, 1]

    def checa_acao(self, acao):
        if acao in self.pacote_acoes():
            return True
        else:
            return False
    
    def read(self):
        return self.estado_texto, self.estado_acao, self.espaco_acoes, self.finalizado

    def imprimeAcao(self, acoes):
        for acao in acoes:
            print("\t{0}".format(acao))


if __name__ == '__main__':
    AMN = AdmiravelMundoNovo()
    estado, acao, dimensao_acao, finalizado = AMN.read()
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
        estado, acao, dimensao_acao, finalizado = AMN.read()
        print(estado)
        AMN.imprimeAcao(acao)
