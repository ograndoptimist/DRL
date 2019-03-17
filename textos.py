ESTADOS = {'estado_1':"\tVocê está na entrada da ilha da Fantasia.  Logo a sua frente há uma ponte\n\tque dá acesso" + 
                      " à entrada do Castelo principal.",
            'estado_2': "\tEntrada do Castelo.\n\tAgora você está na porta principal do Castelo. O Castelo possui 3 andares que você pode explorar" + 
                        "\n\tatravés de belíssimas escadas. Em um desses três andares, está o tesouro que procuras...",
            'estado_3': "\tJardim do Castelo\n\tNo Jardim do Castelo você tem acesso as mais belas plantas de todo o reino." + 
                        " Aqui temos flores, maçãs....e quem sabe uma\n\tpassagem secreta até o tesouro mais procurado nestes tempos....",
            'estado_4': "\tMosteiro dos Bravos Cavalos\n\tVocê pode aproveitar que chegou até aqui e ajudar o zelador a manter os cavalos com" + 
                        " os mais belos cortes de crina.\n\tNo entanto, tomaria cuidado para não tomar um coice, já que aqui também" + 
                        " se\n\tencontram os cavalos mais selvagens do Reino da Ilha da Fantasia...",
            'estado_5': "\tA passagem secreta\n\tDaqui em diante, o teletransporte do castelo se encarrega do trabalho de te aproximar do" +
                        " tesouro que procuras.\n\tTalvez o melhor seja sempre seguir em frente, já que a vida imita a arte...\n\tmas a" +
                        " escolha está em suas mãos...",
            'estado_6': "\tSalão Principal\n\tBem-vindo ao Salão Principal do Castelo. Nosso Castelo está sempre recebendo as mais belas\n\tdivindades" +
                        " do Reino da Fantasia. O tapete vermelho pode te levar ao salão de jantar se você seguir\n\tà esquerda, ou caso contrário, à" + 
                        " direita, você alcança a biblioteca dos mais sábios livros que\n\ttalvez esconda os segredos mais esperados de todo o novo" + 
                        " continente.\n\tTambém há a possibilidade de subir as escadas para se chegar ao próximo andar.",
            'estado_7':"\tSalão de Jantar\n\tOs mais belos jantares são servidos à nobreza do Reino neste local." + 
                       " Somente os de sangue mais\n\tpuro podem utilizar da louça sobre a mesa. O antigo dono da" + 
                       " chave preciosa já esteve por aqui.",
            'estado_8':"\tBiblioteca dos Mais Sábios\n\tPor esta biblioteca já passaram os mais sábios do Reino. Mentes brilhantes produziram" + 
                       " obras\n\tque ficarão por aqui por toda a eternidade. Talvez se você ler todos os livros, será capaz de\n\tencontrar" + 
                       " a reposta do enigma do paradeiro da chave preciosa de ouro.",
            'estado_9': "\tSegundo andar\n\tVocê conseguiu subir as longas escadas do Castelo Principal e chegar ao andar de travessuras.\n\tEste andar" +
                        " é geralmente povoado pelos bobos da corte, então é melhor ficar atento para evitar\n\tapuros com os mais astutos do povoado.",
            'estado_10':"\tTreinamento dos Travessos\n\tCuidado para não atrapalha-los. Aqui eles preparam as melhores perfomances para toda a" + 
                        " corte.",
            'estado_11':"\tDormitório dos Travessos\n\tAté nos sonhos os bobos da corte aprontam as mais astutas travessuras. Se eu fosse você" + 
                        " tomaria\n\tcuidado para não acordá-los, ou é melhor se preparar para se tornar o palhaço da corte...",           
            'estado_12':"\tSantuário dos sonhos esquecidos\n\tOs sonhos mais profundos viajam pelos quartos deste andar. Aqui o inconsciente se comunica" + 
                        " com o\n\tconsciente dos seres do Reino. Dizem por aí que sonharam que a chave estaria por aqui, mas\n\tcabe a você verificar" +
                        " quarto por quarto se é uma verdade ou apenas mais um dos sonhos.",
            'estado_13':"\tO esquecimento profundo\n\tEste quarto traz o esquecimento temporário a quem nele adentra.",
            'estado_final':"\tFinal do jogo.\n\tParabéns! Você conseguiu coletar a chave de ouro preciosa! Sendo assim, o jogo está finalizado!"}


ACOES = {'estado_1':["Atravesse a ponte."],
         'estado_2':["Abra a porta.", "Vá para o leste.", "Vá para o oeste."],
         'estado_3':["Volte para a entrada do Castelo.", "Vá para a passagem secreta."],
         'estado_4':["Volte para a entrada do Castelo."],
         'estado_5':["Seguir em frente.", "Voltar para o jardim."],
         'estado_6':["Suba as escadas.", "Siga à esquerda.", "Siga à direita.", "Volte para a entrada do Castelo."],
         'estado_7':["Volte ao salão principal."],
         'estado_9':["Suba as escadas.", "Siga à esquerda.", "Siga à direita.", "Desça de volta ao primeiro andar."],
         'estado_10':["Volte ao salão principal."],
         'estado_12':["Siga à esquerda.", "Siga à direita."],
         'estado_13':["Volte ao Santuário."],
         'estado_final':[]         
        }


REFORCOS = {'estado_1':0,
            'estado_2':0,
            'estado_3':0,
            'estado_4':0,
            'estado_5':0,
            'estado_6':0,
            'estado_7':0,
            'estado_9':0,
            'estado_10':0,
            'estado_12':0,
            'estado_13':0,
            'estado_final':100
           }


FINALIZADO = {'estado_1':False,                                   
              'estado_final':True
             }

DIMENSOES = {'estado_1':len(ACOES['estado_1']),
             'estado_2':len(ACOES['estado_2']),
             'estado_3':len(ACOES['estado_3']),
             'estado_4':len(ACOES['estado_4']),
             'estado_5':len(ACOES['estado_5']),
             'estado_6':len(ACOES['estado_6']),
             'estado_7':len(ACOES['estado_7']),
             'estado_9':len(ACOES['estado_9']),
             'estado_10':len(ACOES['estado_10']),
             'estado_12':len(ACOES['estado_12']),
             'estado_13':len(ACOES['estado_13']),
             'estado_final':len(ACOES['estado_final'])             
            }
