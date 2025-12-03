#importando bibliotecas 
import sys
import random
import os

#limpa o terminal
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
    
#cria as barras dos indicadores
def barra(nome, valor):
    cheios = int(valor / 5)
    vazios = 20 - cheios
    if software:
        return f"{nome:<14}: [" + "#" * cheios + "·" * vazios + f"] {valor}"
    else:
        return f"{nome:<14}: [" + "#" * cheios + "·" * vazios + f"] "


#função que introduz a interface do jogo
def mostrar_interface(pop, eco, meio, tec):
    limpar_tela() #limpa a rodada anterior

    #printa a nova rodada
    print("=" * 50)
    print("      B S B   E M   C O L A P S O")
    print("=" * 50)

    #barra de status
    print(barra("População", pop))
    print(barra("Economia", eco))
    print(barra("Tecnologia", tec))
    print(barra("Meio-Ambiente", meio))
    print("=" * 50 + "\n")


#mensagens de morte 
def maxTec():
    print('As BigTecs se enraizaram em Brasília e tomaram o controle da cidade\n')
    print('Game Over')

def minTec():
    print('Brasília é considerada a cidade mais mal desenvolvida do Brasil\n')
    print('Game Over')
    
def maxPop():
    print('Mano, sei la\n')
    print('Game Over')
    
def minPop():
    print('A população está revoltada, as ruas estão lotadas e o povo pede por um novo gestor\n')
    print('Game Over')
    
def maxMeio():
    print('As capivaras tomaram o poder\n')
    print('Game Over')
    
def minMeio():
    print('Brasília está em chamas\n')
    print('Game Over')
    
def maxEco():
    print('alguma parada de corrupção ou sla\n')
    print('Game Over')
    
def minEco():
    print('Brasília é a cidade mais pobre do Brasil\n')
    print('Game Over')

#cria todos os eventos do jogo


#verifica se algum dos indices chegou a 0 ou 100 (game over)
def checar_game_over(pop, eco, meio, tec):
    if pop <= 0:
        minPop()
        sys.exit()

    if pop >= 100:
        maxPop()
        sys.exit()

    if eco <= 0:
        minEco()
        sys.exit()

    if eco >= 100:
        maxEco()
        sys.exit()

    if meio <= 00:
        minMeio()
        sys.exit()

    if meio >= 100:
        maxMeio()
        sys.exit()

    if tec <= 0:
        minTec()
        sys.exit()

    if tec >= 100:
        maxTec()
        sys.exit()

def evento1(stats):
    pop, eco, meio, tec = stats

#mensagem de texto do evento
    print(
        'IMPLANTAR WI-FI PÚBLICO EM ÁREAS DE BAIXA RENDA\n'
        'A secretaria de tecnologia propõe instalar Wi-Fi gratuito em regiões carentes.\n'
        'Efeitos: (sim)\n'
        'Tecnologia + \n'
        'Economia - \n'
        'População + \n'
        
        'Efeitos: (nao)\n'
        'População - \n'
        'Tecnologia - \n'
          )

    #lógica de decisão dos eventos
    decisao1 = input('\nDigite "s" ou "n": ').lower()

    eventos.remove(evento1) #remove o evento da lista de eventos possiveis

    while decisao1 not in 'sn': #para casos de resposta inválida
        print('Entrada inválida, tente outra vez\n')
        decisao1 = input('Digite s ou n:').lower()
    
    #alterações nos indices com base na decisão
    if decisao1 == 's':
        tec += 10
        eco -= 10
        pop += 10
        
    elif decisao1 == 'n':
        pop -= 20
        tec -= 10
        
    #retorna os valores novos
    return pop, eco, meio, tec


def evento2(stats):
    pop, eco, meio, tec = stats

    print(
        'IMPLEMENTAR UM SISTEMA DE SEGURANÇA COM IA INTEGRADA\n'
        'A secretaria de segurança pública propôe integrar a IA nos sistemas de câmera de segurança para fazer reconhecimento facial.\n'
        'Efeitos: (sim)\n'
        'Tecnologia + \n'
        'Economia - \n'
        'População + \n'
        
        'Efeitos: (nao)\n'
        'População - \n'
        'Tecnologia - \n'
          )
          
    decisao2 = input('\nDigite "s" ou "n": ').lower()
    eventos.remove(evento2)
    while decisao2 not in 'sn':
        print('Entrada inválida, tente outra vez\n')
        decisao2 = input('Digite s ou n:').lower()

    if decisao2 == 's':
        tec += 20
        eco -= 15
        pop += 10
    elif decisao2 == 'n':
        pop -= 10
        tec -= 20

    return pop, eco, meio, tec


def evento3(stats):
    pop, eco, meio, tec = stats

    print(
        'SUBSTITUIR A FROTA DE ÔNIBUS\n'
        'A secretaria de transporte propõe a substituição de toda a frota de ônibus por ônibus elétricos.\n'
        'Efeitos: (sim)\n'
        'Tecnologia + \n'
        'Economia - \n'
        'Meio-Ambiente + \n'
        
        'Efeitos: (nao)\n'
        'Meio-Ambiente - \n'
        'Tecnologia -\n'
          )
          
    decisao3 = input('\nDigite "s" ou "n": ').lower()
    eventos.remove(evento3)
    while decisao3 not in 'sn':
        print('Entrada inválida, tente outra vez\n')
        decisao3 = input('Digite s ou n:').lower()
    
    if decisao3 == 's':
        eco -= 30
        tec += 10
        meio += 25
    elif decisao3 == 'n':
        tec -= 5
        meio -= 20

    return pop, eco, meio, tec


def evento4(stats):
    pop, eco, meio, tec = stats

    print(
        'ACEITAR CRIPTOMOEDAS COMO FORMA DE PAGAMENTO DE IMPOSTOS\n'
        'Empresas de tecnologia sugerem aceitar criptomoedas no pagamento de taxas públicas.\n'
        'Efeitos: (sim)\n'
        'Economia + \n'
        'Tecnologia - \n'
        
        'Efeitos: (nao)\n'
        'Economia - \n'
          )
          
    decisao4 = input('\nDigite "s" ou "n": ').lower()
    eventos.remove(evento4)
    while decisao4 not in 'sn':
        print('Entrada inválida, tente outra vez\n')
        decisao4 = input('Digite s ou n:').lower()
    

    if decisao4 == 's':
        tec -= 15
        eco += 30
    elif decisao4 == 'n':
        eco -= 10

    return pop, eco, meio, tec

def evento5(stats):
    pop, eco, meio, tec = stats

    print(
        'CONSTRUIR UM SUPER COMPUTADOR.\n'
        'A OPENAI deseja construir um super computador em Brasília.\n'
        'Efeitos: (sim)\n'
        'Economia + \n'
        'Tecnologia + \n'
        'Meio-Ambiente - \n'
        
        'Efeitos: (nao)\n'
        'Economia - \n'
        'Tecnologia - \n'
        'Meio-Ambiente + \n'
          )
          
    decisao5 = input('\nDigite "s" ou "n": ').lower()
    eventos.remove(evento5)
    while decisao5 not in 'sn':
        print('Entrada inválida, tente outra vez\n')
        decisao5 = input('Digite s ou n:').lower()
    

    if decisao5 == 's':
        tec += 20
        eco += 20
        meio -= 25
        eventos.append(evento5A)
    elif decisao5 == 'n':
        eco -= 10
        tec -= 10
        meio += 25

    return pop, eco, meio, tec

def evento5A(stats):
    pop, eco, meio, tec = stats

    print(
        'SUPER AQUECIMENTO.\n'
        'Devido à uma má gestão e o clima de Brasília o super computador da OPEN AI começou a apresentar problemas de super aquecimento. O secretário do meio-ambiente sugere retirar a instalação antes que cause maiores problemas.\n'
        'Efeitos: (sim)\n'
        'Economia - \n'
        'Tecnologia - \n'
        'Meio-Ambiente + \n'
        
        'Efeitos: (nao)\n'
        'Economia + \n'
        'Tecnologia + \n'
        'Meio-Ambiente - \n'
          )
          
    decisao5A = input('\nDigite "s" ou "n": ').lower()
    eventos.remove(evento5A)
    while decisao5A not in 'sn':
        print('Entrada inválida, tente outra vez\n')
        decisao5A = input('Digite s ou n:').lower()
    

    if decisao5A == 's':
        tec -= 20
        eco -= 20
        meio += 25

    elif decisao5A == 'n':
        eco += 10
        tec += 10
        meio -= 25
        eventos.append(evento5B)

    return pop, eco, meio, tec

def evento5B(stats):
    pop, eco, meio, tec = stats

    print(
        'SUPER COMPUTADOR EM CHAMAS.\n'
        'Um incêndio se inicia nas instalações da OPEN AI, ameaçando bairros próximos. deseja enviar grande parte do orçamento emergencial para combate ao incêndio?\n'
        'Efeitos: (sim)\n'
        'Economia - \n'
        'Tecnologia - \n'
        'Meio-Ambiente + \n'
        
        'Efeitos: (nao)\n'
        'Economia + \n'
        'Tecnologia + \n'
        'Meio-Ambiente - \n'
          )
          
    decisao5B = input('\nDigite "s" ou "n": ').lower()
    eventos.remove(evento5B)
    while decisao5B not in 'sn':
        print('Entrada inválida, tente outra vez\n')
        decisao5B = input('Digite s ou n:').lower()
    

    if decisao5B == 's':
        tec -= 25
        eco -= 30
        meio += 30
        
    elif decisao5B == 'n':
        eco += 10
        tec += 10
        meio -= 30
        

    return pop, eco, meio, tec

def evento6(stats):
    pop, eco, meio, tec = stats

    print(
        'REDUÇÃO DE IMPOSTOS.\n'
        'Empresários sugerem reduzir impostos para estimular novos investimentos.\n'
        'Efeitos: (sim)\n'
        'Economia - \n'
        'Tecnologia + \n'
        
        'Efeitos: (nao)\n'
        'Economia + \n'
        'Tecnologia - \n'
          )
          
    decisao6 = input('\nDigite "s" ou "n": ').lower()
    eventos.remove(evento6)
    while decisao6 not in 'sn':
        print('Entrada inválida, tente outra vez\n')
        decisao6 = input('Digite s ou n:').lower()
    

    if decisao6 == 's':
        tec += 20
        eco -= 10
        eventos.append(evento5)
    elif decisao6 == 'n':
        eco += 10
        tec -= 10
        
    return pop, eco, meio, tec

def evento7(stats):
    pop, eco, meio, tec = stats

    print(
        'VAZAMENTO DE DADOS.\n'
        'Um vazamento de dados expos dados de servidores públicos. Deseja investigar?\n'
        'Efeitos: (sim)\n'
        'Nenhum\n'
        
        'Efeitos: (nao)\n'
        'População - \n'
          )
          
    decisao7 = input('\nDigite "s" ou "n": ').lower()

    while decisao7 not in 'sn':
        print('Entrada inválida, tente outra vez\n')
        decisao7 = input('Digite s ou n:').lower()
    
    eventos.remove(evento7)
    if decisao7 == 's':
        eventos.append(evento7A)
    elif decisao7 == 'n':
        pop -= 10
        eventos.append(evento7B)
        
    return pop, eco, meio, tec

def evento7A(stats):
    pop, eco, meio, tec = stats

    print(
        'INVESTIGAÇÃO DO VAZAMENTO DE DADOS.\n'
        'Os hackers culpados foram encontrados e presos. Deseja implementar um sistema de segurança melhor?\n'
        'Efeitos: (sim)\n'
        'Tecnologia + \n'
        'Economia - \n'
        
        'Efeitos: (nao)\n'
        'Nenhum\n'
          )
          
    decisao7A = input('\nDigite "s" ou "n": ').lower()

    while decisao7A not in 'sn':
        print('Entrada inválida, tente outra vez\n')
        decisao7A = input('Digite s ou n:').lower()
        
    eventos.remove(evento7A)
    
    if decisao7A == 's':
        tec += 20
        eco -= 15
    elif decisao7A == 'n':
        eventos.append(evento7)
        
    return pop, eco, meio, tec

def evento7B(stats):
    pop, eco, meio, tec = stats

    print(
        'GRUPO HACKER REINVINDICA AUTORIA.\n'
        'Os hackers responsaveis pelo vazamento de dados exigem mais transparência do governo. Deseja dialogar com eles? \n'
        'Efeitos: (sim)\n'
        'Nenhum\n'
        
        'Efeitos: (nao)\n'
        'Nenhum\n'
          )
          
    decisao7B = input('\nDigite "s" ou "n": ').lower()

    while decisao7B not in 'sn':
        print('Entrada inválida, tente outra vez\n')
        decisao7B = input('Digite s ou n:').lower()
    
    eventos.remove(evento7B)
    
    if decisao7B == 's':
        eventos.append(evento7C)
    elif decisao7B == 'n':
        eventos.append(evento7final)
        
    return pop, eco, meio, tec
                       
def evento7C(stats):
    pop, eco, meio, tec = stats

    print(
        'HACKERS PROPÕEM ACORDO DE PAZ.\n'
        'O grupo hacker propõe cessar os ataques e ajudar em melhorias de segurança caso o governo aceite ter uma maior transpaência com as contas públicas. aceitar acordo?\n'
        'Efeitos: (sim)\n'
        'Tecnologia + \n'
        
        'Efeitos: (nao)\n'
        'Tecnolgia - \n'
          )
          
    decisao7C = input('\nDigite "s" ou "n": ').lower()

    while decisao7C not in 'sn':
        print('Entrada inválida, tente outra vez\n')
        decisao7C = input('Digite s ou n:').lower()
    
    eventos.remove(evento7C)
    
    if decisao7C == 's':
        tec += 25
    elif decisao7C == 'n':
        tec -= 20
        eventos.append(evento7final)
        
    return pop, eco, meio, tec

def evento7final(stats):
    pop, eco, meio, tec = stats

    input(
        'CYBER ATAQUE EM MASSA.\n'
        'TODOS os sistemas públicos caíram, Brasília está um caos!\n'
        'Aperte Enter para continuar'
          )
    print('Game over')
    sys.exit()
          

        
    return pop, eco, meio, tec

def evento8(stats):
    pop, eco, meio, tec = stats

    print(
        'CORTES NO ORÇAMENTO.\n'
        'A equipe de finanças sugere cortar parte do orçamento da saúde para cobrir dívidas.\n'
        'Efeitos: (sim)\n'
        'Economia + \n'
        'População - \n'
        
        'Efeitos: (nao)\n'
        'População + \n'
        'Economia - \n'
          )
          
    decisao8 = input('\nDigite "s" ou "n": ').lower()
    eventos.remove(evento8)
    while decisao8 not in 'sn':
        print('Entrada inválida, tente outra vez\n')
        decisao8 = input('Digite s ou n:').lower()
    

    if decisao8 == 's':
        pop -= 20
        eco += 15
    elif decisao8 == 'n':
        eco -= 10
        pop += 20
        
    return pop, eco, meio, tec

def evento8A(stats):
    pop, eco, meio, tec = stats

    print(
        'MANIFESTANTES LOTAM AS RUAS.\n'
        'Após decisão de cortes de verba da saúde, manifestantes vão às ruas pedindo para revogar a decisão.\n'
        'Efeitos: (sim)\n'
        'Economia - \n'
        'População + \n'
        
        'Efeitos: (nao)\n'
        'População - \n'
        'Economia + \n'
          )
          
    decisao8A = input('\nDigite "s" ou "n": ').lower()
    eventos.remove(evento8A)
    while decisao8A not in 'sn':
        print('Entrada inválida, tente outra vez\n')
        decisao8A = input('Digite s ou n:').lower()
    

    if decisao8A == 's':
        pop += 10
        eco += 20
    elif decisao8A == 'n':
        eco += 20
        pop -= 20
        
    return pop, eco, meio, tec

def evento9(stats):
    pop, eco, meio, tec = stats

    print(
        'CRIAR UM POLO INDUSTRIAL NO GAMA.\n'
        'Indústrias querem se instalar no Gama com incentivos especiais.\n'
        'Efeitos: (sim)\n'
        'Economia + \n'
        'Tecnologia + \n'
        'Meio-Ambiente - \n'
        
        'Efeitos: (nao)\n'
        'Tecnologia - \n'
        'Meio-Ambiente + \n'
          )
          
    decisao9 = input('\nDigite "s" ou "n": ').lower()
    eventos.remove(evento9)
    while decisao9 not in 'sn':
        print('Entrada inválida, tente outra vez\n')
        decisao9 = input('Digite s ou n:').lower()
    

    if decisao9 == 's':
        meio -= 25
        eco += 15
        tec += 15
    elif decisao9 == 'n':
        tec -= 10
        meio += 20
        
    return pop, eco, meio, tec


def evento10(stats):
    pop, eco, meio, tec = stats

    print(
        'APOIO A STARTUP DE TECNOLOGIA.\n'
        'Uma pequena empresa pede por incentivo do governo para desenvolver soluções para Brasília, você deseja apoiar?.\n'
        'Efeitos: (sim)\n'
        'Economia - \n'
        'Tecnologia + \n'

        'Efeitos: (nao)\n'
        'Tecnologia - \n'
        'Economia + \n'
          )
          
    decisao10 = input('\nDigite "s" ou "n": ').lower()
    eventos.remove(evento10)
    while decisao10 not in 'sn':
        print('Entrada inválida, tente outra vez\n')
        decisao10 = input('Digite s ou n:').lower()
    

    if decisao10 == 's':
        eco -= 25
        tec += 20
        eventos.append(evento10A)
        eventos.append(evento10B)
    elif decisao10 == 'n':
        tec -= 10
        eco += 10
        eventos.append(evento15)
        
    return pop, eco, meio, tec

def evento10A(stats):
    pop, eco, meio, tec = stats

    input(
        "LAZULE'S TECH.\n"
        'Olá governador, você decidiu apoiar nosso projeto, queremos mostrar como a tecnologia pode solucionar todos os nossos problemas.\n'
        'Use nosso software para calcular melhor suas decisões\n'
        '\nOS INDICADORES AGORA SERÃO NUMERADOS'
        '\nAperte Enter para continuar'
          )

    global software   
    software = True
    eventos.remove(evento10A)
    return pop, eco, meio, tec

def evento10B(stats):
    pop, eco, meio, tec = stats

    print(
        "LAZULE'S TECH.\n"
        'Olá governador, você decidiu apoiar nosso projeto, queremos mostrar como a tecnologia pode solucionar todos os nossos problemas.\n'
        'Nosso software detectou uma crise hídrica iminente, podemos resolver o problema antes que ele aconteça.\n'
          )
    
    decisao10B = input('\nDigite "s" ou "n": ').lower()
    eventos.remove(evento10B)
    while decisao10 not in 'sn':
        print('Entrada inválida, tente outra vez\n')
        decisao10 = input('Digite s ou n:').lower()

    if decisao10B == 's':
        eco -= 15

    elif decisao10B == 'n':
        eco += 15
        eventos.append(evento15)
    

    return pop, eco, meio, tec

def evento11(stats):
    pop, eco, meio, tec = stats

    input(
        'SECA.\n'
        'Uma grande seca assola Brasília, as queimadas irão aumentar .\n'
        'Efeitos:\n'
        '(Por rodada) Meio-Ambiente -\n '
        'Aperte Enter para continuar'
          )
    global seca
    seca += 4
    eventos.remove(evento11)
        
    return pop, eco, meio, tec

def evento12(stats):
    pop, eco, meio, tec = stats

    print(
        'TARIFA SOCIAL DE ENERGIA.\n'
        'Os moradores pedem por descontos na conta de energia para famílias de baixa renda.\n'
        'Efeitos: (sim)\n'
        'Economia - \n'
        'População + \n'

        'Efeitos: (nao)\n'
        'População - \n'
        'Economia + \n'
          )
          
    decisao12 = input('\nDigite "s" ou "n": ').lower()
    eventos.remove(evento12)
    while decisao12 not in 'sn':
        print('Entrada inválida, tente outra vez\n')
        decisao12 = input('Digite s ou n:').lower()
    

    if decisao12 == 's':
        eco -= 20
        pop += 20
    elif decisao12 == 'n':
        pop -= 20
        eco += 20
        
    return pop, eco, meio, tec

def evento13(stats):
    pop, eco, meio, tec = stats

    print(
        'AUMENTO DA TARIFA DE ÔNIBUS.\n'
        'A equipe de finanças sugere aumentar a tarifa do transporte público.\n'
        'Efeitos: (sim)\n'
        'Economia + \n'
        'População - \n'

        'Efeitos: (nao)\n'
        'População + \n'
        'Economia - \n'
          )
          
    decisao13 = input('\nDigite "s" ou "n": ').lower()

    while decisao13 not in 'sn':
        print('Entrada inválida, tente outra vez\n')
        decisao13 = input('Digite s ou n:').lower()
    
    eventos.remove(evento13)
    if decisao13 == 's':
        eco += 20
        pop -= 15
        eventos.append(evento13A)
    elif decisao13 == 'n':
        pop += 20
        eco -= 15
        
    return pop, eco, meio, tec

def evento13A(stats):
    pop, eco, meio, tec = stats

    print(
        'MANIFESTAÇÃO CONTRA O AUMENTO DA TARIFA DE ÔNIBUS.\n'
        'Manifestantes pressionam para revogar o aumento da tarifa.\n'
        'Efeitos: (sim)\n'
        'Economia - \n'
        'População + \n'

        'Efeitos: (nao)\n'
        'População - \n'
        'Economia + \n'
          )
          
    decisao13A = input('\nDigite "s" ou "n": ').lower()
    eventos.remove(evento13)
    while decisao13A not in 'sn':
        print('Entrada inválida, tente outra vez\n')
        decisao13A = input('Digite s ou n:').lower()
    
    if decisao13A == 's':
        eco -= 30
        pop += 10
        eventos.remove(evento13A)
    elif decisao13A == 'n':
        pop -= 25
        eco += 20
        
    return pop, eco, meio, tec

def evento14(stats):
    pop, eco, meio, tec = stats

    print(
        'INSTALAÇÃO DE ENERGIA SOLAR.\n'
        'Uma empresa europeia oferece instalar uma usina de energia solar no DF com investimento misto público/privado.\n'
        'Efeitos: (sim)\n'
        'Economia - \n'
        'Meio-Ambiente + \n'

        'Efeitos: (nao)\n'
        'Meio-Ambiente - \n'
        'Economia + \n'
          )
          
    decisao14 = input('\nDigite "s" ou "n": ').lower()

    while decisao14 not in 'sn':
        print('Entrada inválida, tente outra vez\n')
        decisao14 = input('Digite s ou n:').lower()
    
    eventos.remove(evento14)
    if decisao14 == 's':
        eco -= 20
        meio += 20
    elif decisao14 == 'n':
        meio -= 20
        eco += 10
        
    return pop, eco, meio, tec

def evento15(stats):
    pop, eco, meio, tec = stats

    input(
        'CRISE HÍDRICA.\n'
        'O reservatório da Barragem do Rio Descoberto atinge nível historicamente baixo! Teremos que fazer racionamento.\n'
        'Efeitos:\n'
        '(Por rodada) População -\n'
        'Aperte Enter para continuar'
          )
    global crise_hidro
    crise_hidro += 3
    eventos.remove(evento15)
        
    return pop, eco, meio, tec

def evento16(stats):
    pop, eco, meio, tec = stats

    print(
        'PROJETO BRASÍLIA VERDE.\n'
        'Após meses de políticas ambientais, você recebe uma proposta da UnB para reflorestar áreas degradadas do DF com participação comunitária.\n'
        'Efeitos: (sim)\n'
        'Economia - \n'
        'Meio-Ambiente + \n'
        'População + \n'

        'Efeitos: (nao)\n'
        'Meio-Ambiente - \n'
        'Economia +\n'
          )
          
    decisao16 = input('\nDigite "s" ou "n": ').lower()
    eventos.remove(evento16)
    while decisao16 not in 'sn':
        print('Entrada inválida, tente outra vez\n')
        decisao16 = input('Digite s ou n:').lower()
    

    if decisao16 == 's':
        eco -= 20
        meio += 20
        pop += 10
    elif decisao16 == 'n':
        meio -= 20
        eco += 10
        
    return pop, eco, meio, tec

def evento17(stats):
    pop, eco, meio, tec = stats

    print(
        'INCÊNDIO NO PARQUE NACIONAL.\n'
        'Um incêndio toma conta do Parque Nacional de Brasília, ameaçando áreas protegidas e bairros próximos. deseja enviar grande parte do orçamento emergencial para combate ao incêndio?\n'
        'Efeitos: (sim)\n'
        'Economia - \n'
        'Meio-Ambiente + \n'
        'População + \n'

        'Efeitos: (nao)\n'
        'Meio-Ambiente - \n'
        'Economia + \n'
        'População - \n'
          )
          
    
    decisao17 = input('\nDigite "s" ou "n": ').lower()
    eventos.remove(evento17)
    while decisao17 not in 'sn':
        print('Entrada inválida, tente outra vez\n')
        decisao17 = input('Digite s ou n:').lower()
    

    if decisao17 == 's':
        eco -= 35
        meio += 20
        pop += 20
    elif decisao17 == 'n':
        meio -= 35
        eco += 20
        pop -= 15
        
    return pop, eco, meio, tec

def evento18(stats):
    pop, eco, meio, tec = stats

    print(
        'DRONES DE ENTREGA.\n'
        'A Amazon quer instalar um sistema de entrega mais veloz utilizando drones.\n'
        'Efeitos: (sim)\n'
        'Economia + \n'
        'Meio-Ambiente - \n'
        'População + \n'

        'Efeitos: (nao)\n'
        'Meio-Ambiente + \n'
        'Economia - \n'
        'População - \n'
          )
          
    decisao18 = input('\nDigite "s" ou "n": ').lower()
    eventos.remove(evento18)
    while decisao18 not in 'sn':
        print('Entrada inválida, tente outra vez\n')
        decisao18 = input('Digite s ou n:').lower()
    

    if decisao18 == 's':
        eco += 25
        meio -= 20
        pop += 10
    elif decisao18 == 'n':
        meio += 20
        eco -= 15
        pop -= 10
        
    return pop, eco, meio, tec

def evento19(stats):
    pop, eco, meio, tec = stats

    print(
        'MODERNIZAÇÃO DO ENSINO.\n'
        'A secretaria de educação propõe implementar computadores em todas as escolas da rede pública.\n'
        'Efeitos: (sim)\n'
        'Economia - \n'
        'Tecnologia + \n'
        'População + \n'

        'Efeitos: (nao)\n'
        'Economia + \n'
        'Tecnologia - \n'
        'População - \n'
          )
          
    decisao19 = input('\nDigite "s" ou "n": ').lower()
    eventos.remove(evento19)
    while decisao19 not in 'sn':
        print('Entrada inválida, tente outra vez\n')
        decisao19 = input('Digite s ou n:').lower()
    

    if decisao19 == 's':
        eco -= 30
        tec += 20
        pop -= 10
    elif decisao19 == 'n':
        tec -= 10
        eco += 20
        pop -= 10
        
    return pop, eco, meio, tec

#lista de todos os eventos possiveis
eventos = [
    evento1, evento2, evento3, evento4,
    evento6, evento7, evento8, evento9, evento10,
    evento11, evento12, evento13, evento14,
    evento16, evento17, evento18, evento19
    ]

#inicia a rodada
def rodada():
    pop = eco = meio = tec = 50 #indices base para iniciar o jogo
    
    #eventos de longa duração
    global seca
    tempo_seca = 0
    seca = 0
    
    global crise_hidro
    tempo_hidro = 0
    crise_hidro = 0

    global software
    software = False
    
    while True:
        
        #checa se os eventos de longa duração terminaram
        if tempo_seca == 4:
            input('\nChuva! A seca finalmente acabou!')
            tempo_seca -=4
            
        if tempo_hidro == 3:
            input('\nO reservatório está cheio novamente! Acabou o racionamento de água!')
            tempo_hidro -=3
            
        #mostra a interface do jogo com as barras de indicadores
        mostrar_interface(pop, eco, meio, tec)

        #verifica se o jogador perdeu
        checar_game_over(pop, eco, meio, tec)
        
        #checa se a lista de eventos está vazia antes de escolher um evento aleatório
        if (eventos) == 0:
            input('Parabéns você sobreviveu ao mandato!\nAperte Enter para encerrar.')
            sys.exit()

        else:
            evento_escolhido = random.choice(eventos)
            pop, eco, meio, tec = evento_escolhido((pop, eco, meio, tec))
        
        #temporizador dos eventos de longa duração
        if seca != 0:
            meio -= 5
            seca -= 1
            tempo_seca += 1
            
        if crise_hidro != 0:
            pop -= 5
            crise_hidro -= 1
            tempo_hidro += 1
        

#introdução do jogo
print('Você é o gestor de Brasília e precisa administrar a cidade\n')

while True:
    resposta = input('Aperte Enter para continuar no jogo! ')
    if resposta == '':
        break
    print('Entrada inválida! Pressione apenas Enter para continuar.\n')

print('\nSeu trabalho é equilibrar as 4 forças que regem a sociedade:\n Economia\n População\n Tecnologia\n Meio Ambiente\n')

while True:
    resposta = input('Aperte Enter para iniciar\n')
    if resposta == '':
        break
    print('Entrada inválida! Pressione apenas Enter para iniciar.\n')

#start
rodada()
