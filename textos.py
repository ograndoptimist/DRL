ESTADOS = {'estado_inicial':"\tPrimeiro desafio\n\tVocê está na entrada da ilha da Fantasia. O objetivo do jogo é coletar a chave preciosa de ouro" + 
                            ".\n\tPara tal, você precisa vasculhar os andares do Castelo Principal. Logo a sua frente há uma ponte\n\tque dá acesso" + 
                            " à entrada do Castelo principal.",
            'estado_1': "\tEntrada do Castelo.\n\tAgora você está na porta principal do Castelo. O Castelo possui 3 andares que você pode explorar" + 
                        "\n\tatravés de belíssimas escadas. Em um desses três andares, está o tesouro que procuras...",
            'estado_leste': "\tJardim do Castelo\n\tNo Jardim do Castelo você tem acesso as mais belas plantas de todo o reino." + 
                            " Aqui temos flores, maçãs....e quem sabe uma\n\tpassagem secreta até o tesouro mais procurado nestes tempos....",
            'estado_oeste': "\tMosteiro dos Bravos Cavalos\n\tVocê pode aproveitar que chegou até aqui e ajudar o zelador a manter os cavalos com" + 
                            " os mais belos cortes de crina.\n\tNo entanto, tomaria cuidado para não tomar um coice, já que aqui também" + 
                            " se\n\tencontram os cavalos mais selvagens do Reino da Ilha da Fantasia...",
            'estado_passagem_secreta': "\tA passagem secreta\n\tDaqui em diante, o teletransporte do castelo se encarrega do trabalho de te aproximar do" +
                                       " tesouro que procuras.\n\tTalvez o melhor seja sempre seguir em frente, já que a vida imita a arte...\n\tmas a" +
                                       " escolha está em suas mãos...",
            'estado_2': "\tSalão Principal\n\tBem-vindo ao Salão Principal do Castelo. Nosso Castelo está sempre recebendo as mais belas\n\tdivindades" +
                        " do Reino da Fantasia. O tapete vermelho pode te levar ao salão de jantar se você seguir\n\tà esquerda, ou caso contrário, à" + 
                        " direita, você alcança a biblioteca dos mais sábios livros que\n\ttalvez esconda os segredos mais esperados de todo o novo" + 
                        " continente.\n\tTambém há a possibilidade de subir as escadas para se chegar ao próximo andar.",
            'estado_2_esquerda':"\tSalão de Jantar\n\tOs mais belos jantares são servidos à nobreza do Reino neste local." + 
                                " Somente os de sangue mais\n\tpuro podem utilizar da louça sobre a mesa. O antigo dono da" + 
                                " chave preciosa já esteve por aqui.",
            'estado_2_direita':"\tBiblioteca dos Mais Sábios\n\tPor esta biblioteca já passaram os mais sábios do Reino. Mentes brilhantes produziram" + 
                               " obras\n\tque ficarão por aqui por toda a eternidade. Talvez se você ler todos os livros, será capaz de\n\tencontrar" + 
                               " a reposta do enigma do paradeiro da chave preciosa de ouro.",
            'estado_3': "\tSegundo andar\n\tVocê conseguiu subir as longas escadas do Castelo Principal e chegar ao andar de travessuras.\n\tEste andar" +
                        " é geralmente povoado pelos bobos da corte, então é melhor ficar atento para evitar\n\tapuros com os mais astutos do povoado.",
            'estado_3_esquerda':"\tTreinamento dos Travessos\n\tCuidado para não atrapalha-los. Aqui eles preparam as melhores perfomances para toda a" + 
                                " corte.",
            'estado_3_direita':"\tDormitório dos Travessos\n\tAté nos sonhos os bobos da corte aprontam as mais astutas travessuras. Se eu fosse você" + 
                               " tomaria\n\tcuidado para não acordá-los, ou é melhor se preparar para se tornar o palhaço da corte...",
            'estado_4':"\tSantuário dos sonhos esquecidos\n\tOs sonhos mais profundos viajam pelos quartos deste andar. Aqui o inconsciente se comunica" + 
                       " com o\n\tconsciente dos seres do Reino. Dizem por aí que sonharam que a chave estaria por aqui, mas\n\tcabe a você verificar" +
                       " quarto por quarto se é uma verdade ou apenas mais um dos sonhos.",
            'estado_4_esquerda':"\tO esquecimento profundo\n\tEste quarto traz o esquecimento temporário a quem nele adentra.",
            'estado_final':"\tFinal do jogo.\n\tParabéns! Você conseguiu coletar a chave de ouro preciosa! Sendo assim, o jogo está finalizado!"}


ACOES = {'estado_inicial':["Atravesse a ponte."],
         'estado_1':["Abra a porta.", "Vá para o leste.", "Vá para o oeste."],
         'estado_leste':["Volte para a entrada do Castelo.", "Vá para a passagem secreta."],
         'estado_oeste':["Volte para a entrada do Castelo."],
         'estado_passagem_secreta':["Seguir em frente.", "Voltar para o jardim."],
         'estado_2':["Suba as escadas.", "Siga à esquerda.", "Siga à direita."],
         'estado_2_esquerda_direita':["Volte ao salão principal."],
         'estado_3':["Suba as escadas.", "Siga à esquerda.", "Siga à direita."],
         'estado_3_esquerda_direita':["Volte ao salão principal."],
         'estado_4':["Siga à esquerda.", "Siga à direita."],
         'estado_4_esquerda':["Volte ao Santuário."],
         'estado_final':[]         
        }


REFORCOS = {'estado_inicial':0,
            'estado_1':1,
            'estado_leste':1,
            'estado_oeste':0,
            'estado_passagem_secreta':10,
            'estado_2':1,
            'estado_2_esquerda_direita':0,
            'estado_3':1,
            'estado_3_esquerda_direita':0,
            'estado_4':1,
            'estado_4_esquerda':-10,
            'estado_final':100
           }


FINALIZADO = {'estado_inicial':False,                                   
              'estado_final':True
             }

DIMENSOES = {'estado_inicial':len(ACOES['estado_inicial']),
             'estado_1':len(ACOES['estado_1']),
             'estado_leste':len(ACOES['estado_leste']),
             'estado_oeste':len(ACOES['estado_oeste']),
             'estado_passagem_secreta':len(ACOES['estado_passagem_secreta']),
             'estado_2':len(ACOES['estado_2']),
             'estado_2_esquerda_direita':len(ACOES['estado_2_esquerda_direita']),
             'estado_3':len(ACOES['estado_3']),
             'estado_3_esquerda_direita':len(ACOES['estado_3_esquerda_direita']),
             'estado_4':len(ACOES['estado_4']),
             'estado_4_esquerda':len(ACOES['estado_4_esquerda']),
             'estado_final':len(ACOES['estado_final'])             
            }
