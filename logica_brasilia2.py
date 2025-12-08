#importando bibliotecas 
import sys
import random
import os
import time
from colorama import Fore, init


def print_event(block):
    try:
        init()
    except Exception:
        pass
    for raw in block.splitlines():
        line = raw.rstrip()
        if line.strip().endswith('+'):
            print(Fore.GREEN + line + Fore.WHITE)
        elif line.strip().endswith('-'):
            print(Fore.RED + line + Fore.WHITE)
        else:
            print(line)


#tela inicial do jogo
def tela_inicial():
    limpar_tela()
    print("=" * 40)
    print(' ' * 12 + Fore.YELLOW +"BSB EM COLAPSO" + Fore.WHITE)
    print("=" * 40)

    print(Fore.BLACK+ ''' 
                        .|
                       | |
                       |'|            
               ___    |  |           
       _    .-'   '-. |  |     .--'| 
    .-'|  _.|  |    ||   '-__  |   |  
    |' | |.    |    ||       | |   | 
 ___|  '-'     '    ''       '-'   '-
        ''' + Fore.WHITE )
    print("=" * 40)
    print("1 - INICIAR JOGO")
    print("2 - Créditos")
    print("0 - Sair")
    print("=" * 40)

def Menu():
    while True:
        tela_inicial()
        opc = input("Escolha uma opção: ").strip()

        if opc == "1":
            limpar_tela()
            print("Iniciando novo jogo...")
            time.sleep(1)
            limpar_tela()
            print("=" * 40)
            print("       C O M O   J O G A R:" )
            print("=" * 40)
            print("Você é o gestor de Brasília e precisa equilibrar as 4 forças que regem a sociedade:\n"
                "\n[ P O P U L A Ç Ã O ] (Nível de popularidade e satisfação do povo com a gestão)\n"
                "[ E C O N O M I A ] (Quantidade de dinheiro nos cofres públicos)\n"
                "[ T E C N O L O G I A ] (Nível de desenvolvimento tecnológico da cidade)\n"
                "[ M E I O - A M B I E N T E ] (Qualidade do meio-ambiente)\n"
                "\nSeu trabalho é garantir que nenhum dos 4 indicadores chegue ao máximo ou ao mínimo, mantendo a barra do indicador sempre entre 1% e 99%"
                "\nCada escolha irá impactar diminuindo ou aumetando os indicadores e possuem desdobramentos narrativos diferentes."
                )
            print("=" * 40 + "\n")
            input("\nPressione Enter para continuar...")
            break

        elif opc == "2":
            limpar_tela()
            print(
                "TRABALHO FINAL DE APC\n"
                "\nDesenvolvido por:\n"
                "Pedro vítor de Mendonça Furtado\n"
                "Gusthavo de Oliveira Silva\n"
                "Marco Antônio lopes de Medeiros\n"
                "Gabriel Peres de Oliveira\n"
                )

            input("\nPressione Enter para voltar...")
        elif opc == "0":
            limpar_tela()
            print("Saindo...")
            time.sleep(1)
            sys.exit()
            break
        else:
            print("Opção inválida.")
            time.sleep(1)
    
    rodada()

#limpa o terminal
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
    
#cria as barras dos indicadores
def barra(nome, valor):
    cheios = int(valor / 5)
    vazios = 20 - cheios
    if software:
        return f"{nome:<14}: [" + Fore.YELLOW + "#" * cheios + Fore.WHITE + "·" * vazios + f"] {valor}"
    else:
        return f"{nome:<14}: [" + Fore.YELLOW + "#" * cheios + Fore.WHITE + "·" * vazios + f"] "


#função que introduz a interface do jogo
def mostrar_interface(pop, eco, meio, tec):
    limpar_tela() #limpa a rodada anterior

    #printa a nova rodada
    print("=" * 50)
    print(" " * 15 + Fore.YELLOW + "I N D I C A D O R E S" + Fore.WHITE)
    print("=" * 50)

    #barra de status
    print(barra("População", pop))
    print(barra("Economia", eco))
    print(barra("Tecnologia", tec))
    print(barra("Meio-Ambiente", meio))
    print("=" * 50 + "\n")


#mensagens de morte 
def maxTec():
    print('As BigTecs se enraizaram em Brasília. A única opção é se render aos interesses privados.\n')
    print('\nGAME OVER\n')
    time.sleep(1)
    input("\nPressione Enter para voltar ao Menu...")

def minTec():
    print('Brasília é considerada a cidade mais mal desenvolvida do Brasil.\n')
    print('\nGAME OVER\n')
    time.sleep(1)
    input("\nPressione Enter para voltar ao Menu...")
    
def maxPop():
    print('Você se tornou super popular, mas a fama também trás coisas ruins. Você foi assassinado enquanto discursava em público.\n')
    print('\nGAME OVER\n')
    time.sleep(1)
    input("\nPressione Enter para voltar ao Menu...")
    
def minPop():
    print('A população está revoltada, as ruas estão lotadas e o povo pede por um novo gestor.\n')
    print('\nGAME OVER\n')
    time.sleep(1)
    input("\nPressione Enter para voltar ao Menu...")
    
def maxMeio():
    print('As capivaras tomaram o poder. Todos se recusam a machucar um animal tão fofinho, o que resta é se render.\n')
    print('\nGAME OVER\n')
    time.sleep(1)
    input("\nPressione Enter para voltar ao Menu...")
    
def minMeio():
    print('Brasília está em chamas.\n')
    print('\nGAME OVER\n')
    time.sleep(1)
    input("\nPressione Enter para voltar ao Menu...")
    
def maxEco():
    print('Você está sendo investigado por corrupção. Sua populariade caiu e o povo pede por um novo gestor.\n')
    print('\nGAME OVER\n')
    time.sleep(1)
    input("\nPressione Enter para voltar ao Menu...")

    
def minEco():
    print('Brasília é a cidade mais pobre do Brasil. O povo pede por um novo gestor.\n')
    print('\nGAME OVER\n')
    time.sleep(1)
    input("\nPressione Enter para voltar ao Menu...")

#cria todos os eventos do jogo


#verifica se algum dos indices chegou a 0 ou 100 (GAME OVER)
def checar_game_over(pop, eco, meio, tec):
    if pop <= 0:
        minPop()
        Menu()

    if pop >= 100:
        maxPop()
        Menu()

    if eco <= 0:
        minEco()
        Menu()

    if eco >= 100:
        maxEco()
        Menu()

    if meio <= 00:
        minMeio()
        Menu()

    if meio >= 100:
        maxMeio()
        Menu()

    if tec <= 0:
        minTec()
        Menu()

    if tec >= 100:
        maxTec()
        Menu()

#lista de todos os eventos possiveis
def evento1(stats):
    pop, eco, meio, tec = stats

#mensagem de texto do evento
    print(
        'IMPLANTAR WI-FI PÚBLICO EM ÁREAS DE BAIXA RENDA\n'
        'A secretaria de tecnologia propõe instalar Wi-Fi gratuito em regiões carentes. Deseja aprovar?\n'
        '\nEfeitos: (sim)\n' +
        Fore.GREEN + 'Tecnologia + \n' +
        Fore.RED + 'Economia - \n' +
        Fore.GREEN + 'População + \n' +
        
        Fore.WHITE +'\nEfeitos: (não)\n' +
        Fore.RED + 'População - \n' +
        Fore.RED +'Tecnologia - \n' + Fore.WHITE
          )

    #lógica de decisão dos eventos
    decisao1 = input('Digite "s" (sim) ou "n" (não): ').lower()

    eventos.remove(evento1) #remove o evento da lista de eventos possiveis
    
    while decisao1 not in 'sn' or decisao1 == "": #para casos de resposta inválida
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

    print_event(
        'IMPLEMENTAR UM SISTEMA DE SEGURANÇA COM IA INTEGRADA\n'
        'A secretaria de segurança pública propôe integrar a IA nos sistemas de câmera de segurança para fazer reconhecimento facial. Deseja aprovar?\n'
        '\nEfeitos: (sim)\n'
        'Tecnologia + \n'
        'Economia - \n'
        'População + \n'
        
        '\nEfeitos: (não)\n'
        'População - \n'
        'Tecnologia - \n'
          )
          
    decisao2 = input('\nDigite "s" (sim) ou "n" (não): ').lower()
    eventos.remove(evento2)
    while decisao2 not in 'sn' or decisao2 == "":
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

    print_event(
        'SUBSTITUIR A FROTA DE ÔNIBUS\n'
        'A secretaria de transporte propõe a substituição de toda a frota de ônibus por ônibus elétricos. Deseja aprovar?\n'
        '\nEfeitos: (sim)\n'
        'Tecnologia + \n'
        'Economia - \n'
        'Meio-Ambiente + \n'
        
        '\nEfeitos: (não)\n'
        'Meio-Ambiente - \n'
        'Tecnologia -\n'
          )
          
    decisao3 = input('\nDigite "s" (sim) ou "n" (não): ').lower()
    eventos.remove(evento3)
    while decisao3 not in 'sn' or decisao3 == "":
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

    print_event(
        'ACEITAR CRIPTOMOEDAS COMO FORMA DE PAGAMENTO DE IMPOSTOS\n'
        'Empresas de tecnologia sugerem aceitar criptomoedas no pagamento de taxas públicas. Deseja aprovar?\n'
        '\nEfeitos: (sim)\n'
        'Economia + \n'
        'Tecnologia - \n'
        
        '\nEfeitos: (não)\n'
        'Economia - \n'
          )
          
    decisao4 = input('\nDigite "s" (sim) ou "n" (não): ').lower()
    eventos.remove(evento4)
    while decisao4 not in 'sn' or decisao4 == "":
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

    print_event(
        'CONSTRUIR UM SUPER COMPUTADOR.\n'
        'A OPENAI deseja construir um super computador em Brasília. Deseja aprovar? \n'
        '\nEfeitos: (sim)\n'
        'Economia + \n'
        'Tecnologia + \n'
        'Meio-Ambiente - \n'
        
        '\nEfeitos: (não)\n'
        'Economia - \n'
        'Tecnologia - \n'
        'Meio-Ambiente + \n'
          )
          
    decisao5 = input('\nDigite "s" ou "n": ').lower()
    eventos.remove(evento5)
    while decisao5 not in 'sn' or decisao5 == "":
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

    print_event(
        'SUPER AQUECIMENTO.\n'
        'Devido à uma má gestão e o clima de Brasília o super computador da OPEN AI começou a apresentar problemas de super aquecimento. O secretário do meio-ambiente sugere retirar a instalação antes que cause maiores problemas. Deseja aprovar?\n'
        '\nEfeitos: (sim)\n'
        'Economia - \n'
        'Tecnologia - \n'
        'Meio-Ambiente + \n'
        
        '\nEfeitos: (não)\n'
        'Economia + \n'
        'Tecnologia + \n'
        'Meio-Ambiente - \n'
          )
          
    decisao5A = input('\nDigite "s" (sim) ou "n" (não): ').lower()
    eventos.remove(evento5A)
    while decisao5A not in 'sn' or decisao5A == "":
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

    print_event(
        'SUPER COMPUTADOR EM CHAMAS.\n'
        'Um incêndio se inicia nas instalações da OPEN AI, ameaçando bairros próximos. Deseja enviar grande parte do orçamento emergencial para combate ao incêndio?\n'
        '\nEfeitos: (sim)\n'
        'Economia - \n'
        'Tecnologia - \n'
        'Meio-Ambiente + \n'
        
        '\nEfeitos: (não)\n'
        'Economia + \n'
        'Tecnologia + \n'
        'Meio-Ambiente - \n'
          )
          
    decisao5B = input('\nDigite "s" (sim) ou "n" (não): ').lower()
    eventos.remove(evento5B)
    while decisao5B not in 'sn' or decisao5B == "":
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

    print_event(
        'REDUÇÃO DE IMPOSTOS.\n'
        'Empresários sugerem reduzir impostos para estimular novos investimentos. Deseja reduzir os impostos?\n'
        '\nEfeitos: (sim)\n'
        'Economia - \n'
        'Tecnologia + \n'
        
        '\nEfeitos: (não)\n'
        'Economia + \n'
        'Tecnologia - \n'
          )
          
    decisao6 = input('\nDigite "s" (sim) ou "n" (não): ').lower()
    eventos.remove(evento6)
    while decisao6 not in 'sn' or decisao6 == "":
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

    print_event(
        'VAZAMENTO DE DADOS.\n'
        'Um vazamento de dados expos dados de servidores públicos. Deseja investigar?\n'
        '\nEfeitos: (sim)\n'
        'Economia -\n'
        
        '\nEfeitos: (não)\n'
        'População - \n'
          )
          
    decisao7 = input('\nDigite "s" (sim) ou "n" (não): ').lower()

    while decisao7 not in 'sn' or decisao7 == "":
        print('Entrada inválida, tente outra vez\n')
        decisao7 = input('Digite s ou n:').lower()
    
    eventos.remove(evento7)
    if decisao7 == 's':
        eventos.append(evento7A)
        eco -= 10
    elif decisao7 == 'n':
        pop -= 10
        eventos.append(evento7B)
        
    return pop, eco, meio, tec

def evento7A(stats):
    pop, eco, meio, tec = stats

    print_event(
        'INVESTIGAÇÃO DO VAZAMENTO DE DADOS.\n'
        'Os hackers culpados foram encontrados e presos. Deseja implementar um sistema de segurança melhor?\n'
        '\nEfeitos: (sim)\n'
        'Tecnologia + \n'
        'Economia - \n'
        
        '\nEfeitos: (não)\n'
        'Nenhum\n'
          )
          
    decisao7A = input('\nDigite "s" (sim) ou "n" (não): ').lower()

    while decisao7A not in 'sn' or decisao7A == "":
        print('Entrada inválida, tente outra vez\n')
        decisao7A = input('Digite s ou n:').lower()
        
    eventos.remove(evento7A)
    
    if decisao7A == 's':
        tec += 20
        eco -= 15
    elif decisao7A == 'n':
        eventos.append(evento7final)
        
    return pop, eco, meio, tec

def evento7B(stats):
    pop, eco, meio, tec = stats

    print_event(
        'GRUPO HACKER REINVINDICA AUTORIA.\n'
        'Os hackers responsaveis pelo vazamento de dados exigem mais transparência do governo. Deseja dialogar? \n'
        '\nEfeitos: (sim)\n'
        'Nenhum\n'
        
        '\nEfeitos: (não)\n'
        'Nenhum\n'
          )
          
    decisao7B = input('\nDigite "s"(sim) ou "n" (não): ').lower()

    while decisao7B not in 'sn' or decisao7B == "":
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

    print_event(
        'HACKERS PROPÕEM ACORDO DE PAZ.\n'
        'O grupo hacker propõe cessar os ataques e ajudar em melhorias de segurança caso o governo aceite ter uma maior transpaência com as contas públicas. Aceitar acordo?\n'
        '\nEfeitos: (sim)\n'
        'Tecnologia + \n'
        
        '\nEfeitos: (não)\n'
        'Tecnolgia - \n'
          )
          
    decisao7C = input('\nDigite "s" (sim) ou "n" (não): ').lower()

    while decisao7C not in 'sn' or decisao7C == "":
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

    print(
        'CYBER ATAQUE EM MASSA.\n'
        'TODOS os sistemas públicos caíram, Brasília está um caos!')
    print(Fore.GREEN +'''
     _.--""--._
    /  _    _  \ 
 _  ( (_\  /_) )  _
{ \._\   /\   /_./ }
(_"=-.}______{.-="_) 
 _  _.=("""")=._  _
(_'"_.-"`~~`"-._"'_)
 {_"            "_}
    ''''G4ME 0VER' + Fore.WHITE
    )
    input('\nAperte Enter para continuar...')
    Menu()
          

        
    return pop, eco, meio, tec

def evento8(stats):
    pop, eco, meio, tec = stats

    print_event(
        'CORTES NO ORÇAMENTO.\n'
        'A equipe de finanças sugere cortar parte do orçamento da saúde para cobrir dívidas. Deseja aprovar?\n'
        '\nEfeitos: (sim)\n'
        'Economia + \n'
        'População - \n'
        
        '\nEfeitos: (não)\n'
        'População + \n'
        'Economia - \n'
          )
          
    decisao8 = input('\nDigite "s" (sim) ou "n" (não): ').lower()
    eventos.remove(evento8)
    while decisao8 not in 'sn' or decisao8 == "":
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

    print_event(
        'MANIFESTANTES LOTAM AS RUAS.\n'
        'Após decisão de cortes de verba da saúde, manifestantes vão às ruas pedindo para revogar a decisão. Deseja revogar?\n'
        '\nEfeitos: (sim)\n'
        'Economia - \n'
        'População + \n'
        
        '\nEfeitos: (não)\n'
        'População - \n'
        'Economia + \n'
          )
          
    decisao8A = input('\nDigite "s" (sim) ou "n" (não): ').lower()
    eventos.remove(evento8A)
    while decisao8A not in 'sn' or decisao8A == "":
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

    print_event(
        'CRIAR UM POLO INDUSTRIAL NO GAMA.\n'
        'Indústrias querem se instalar no Gama com incentivos especiais. Deseja aprovar?\n'
        '\nEfeitos: (sim)\n'
        'Economia + \n'
        'Tecnologia + \n'
        'Meio-Ambiente - \n'
        
        '\nEfeitos: (não)\n'
        'Tecnologia - \n'
        'Meio-Ambiente + \n'
          )
          
    decisao9 = input('\nDigite "s" (sim) ou "n" (não): ').lower()
    eventos.remove(evento9)
    while decisao9 not in 'sn' or decisao9 == "":
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

    print_event(
        "LAZULES's TECH.\n"
        'Uma pequena empresa pede por incentivo do governo para desenvolver soluções para Brasília, você deseja apoiar?.\n'
        '\nEfeitos: (sim)\n'
        'Economia - \n'
        'Tecnologia + \n'

        '\nEfeitos: (não)\n'
        'Tecnologia - \n'
        'Economia + \n'
          )
          
    decisao10 = input('\nDigite "s" (sim) ou "n" (não): ').lower()
    eventos.remove(evento10)
    while decisao10 not in 'sn' or decisao10 == "":
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
        'Nosso software detectou uma crise hídrica iminente, podemos resolver o problema antes que ele aconteça. Deseja investir?\n'
          )
    
    decisao10B = input('\nDigite "s" (sim) ou "n" (não): ').lower()
    eventos.remove(evento10B)
    while decisao10B not in 'sn' or decisao10B == "":
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
        'Efeitos: (Por rodada)\n' +
        Fore.RED +'Meio-Ambiente -\n '+ Fore.WHITE +
        '\nAperte Enter para continuar'
          )
    global seca
    seca += 4
    eventos.remove(evento11)
        
    return pop, eco, meio, tec

def evento12(stats):
    pop, eco, meio, tec = stats

    print_event(
        'TARIFA SOCIAL DE ENERGIA.\n'
        'Os moradores pedem por descontos na conta de energia para famílias de baixa renda. Deseja aprovar?\n'
        '\nEfeitos: (sim)\n'
        'Economia - \n'
        'População + \n'

        '\nEfeitos: (não)\n'
        'População - \n'
        'Economia + \n'
          )
          
    decisao12 = input('\nDigite "s" (sim) ou "n" (não): ').lower()
    eventos.remove(evento12)
    while decisao12 not in 'sn' or decisao12 == "":
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

    print_event(
        'AUMENTO DA TARIFA DE ÔNIBUS.\n'
        'A equipe de finanças sugere aumentar a tarifa do transporte público. Deseja aprovar?\n'
        '\nEfeitos: (sim)\n'
        'Economia + \n'
        'População - \n'

        '\nEfeitos: (não)\n'
        'População + \n'
        'Economia - \n'
          )
          
    decisao13 = input('\nDigite "s" (sim) ou "n" (não): ').lower()

    while decisao13 not in 'sn' or decisao13 == "":
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

    print_event(
        'MANIFESTAÇÃO CONTRA O AUMENTO DA TARIFA DE ÔNIBUS.\n'
        'Manifestantes pressionam para revogar o aumento da tarifa. Deseja revogar?\n'
        '\nEfeitos: (sim)\n'
        'Economia - \n'
        'População + \n'

        '\nEfeitos: (não)\n'
        'População - \n'
        'Economia + \n'
          )
          
    decisao13A = input('\nDigite "s"(sim) ou "n" (não): ').lower()
    while decisao13A not in 'sn' or decisao13A == "":
        print('Entrada inválida, tente outra vez\n')
        decisao13A = input('Digite s ou n:').lower()
    
    if decisao13A == 's':
        eco -= 25
        pop += 10
        eventos.remove(evento13A)
    elif decisao13A == 'n':
        pop -= 25
        eco += 20
        
    return pop, eco, meio, tec

def evento14(stats):
    pop, eco, meio, tec = stats

    print_event(
        'INSTALAÇÃO DE ENERGIA SOLAR.\n'
        'Uma empresa europeia oferece instalar uma usina de energia solar no DF com investimento misto público/privado. Deseja aprovar?\n'
        '\nEfeitos: (sim)\n'
        'Economia - \n'
        'Meio-Ambiente + \n'

        '\nEfeitos: (não)\n'
        'Meio-Ambiente - \n'
        'Economia + \n'
          )
          
    decisao14 = input('\nDigite "s" (sim) ou "n" (não): ').lower()

    while decisao14 not in 'sn' or decisao14 == "":
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
        'Efeitos: (Por rodada) \n' +
        Fore.RED + 'População -\n' + Fore.WHITE +
        '\nAperte Enter para continuar'
          )
    global crise_hidro
    crise_hidro += 3
    eventos.remove(evento15)
        
    return pop, eco, meio, tec

def evento16(stats):
    pop, eco, meio, tec = stats

    print_event(
        'PROJETO BRASÍLIA VERDE.\n'
        'Após meses de políticas ambientais, você recebe uma proposta da UnB para reflorestar áreas degradadas do DF com participação comunitária. Deseja aprovar? \n'
        '\nEfeitos: (sim)\n'
        'Economia - \n'
        'Meio-Ambiente + \n'
        'População + \n'

        '\nEfeitos: (não)\n'
        'Meio-Ambiente - \n'
        'Economia +\n'
          )
          
    decisao16 = input('\nDigite "s" (sim) ou "n" (não): ').lower()
    eventos.remove(evento16)
    while decisao16 not in 'sn' or decisao16 == "":
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

    print_event(
        'INCÊNDIO NO PARQUE NACIONAL.\n'
        'Um incêndio toma conta do Parque Nacional de Brasília, ameaçando áreas protegidas e bairros próximos. Deseja enviar grande parte do orçamento emergencial para combate ao incêndio?\n'
        '\nEfeitos: (sim)\n'
        'Economia - \n'
        'Meio-Ambiente + \n'
        'População + \n'

        '\nEfeitos: (não)\n'
        'Meio-Ambiente - \n'
        'Economia + \n'
        'População - \n'
          )
          
    
    decisao17 = input('\nDigite "s" (sim) ou "n" (não): ').lower()
    eventos.remove(evento17)
    while decisao17 not in 'sn' or decisao17 == "":
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

    print_event(
        'DRONES DE ENTREGA.\n'
        'A Amazon quer instalar um sistema de entrega mais veloz utilizando drones Deseja aprovar?.\n'
        '\nEfeitos: (sim)\n'
        'Economia + \n'
        'Meio-Ambiente - \n'
        'População + \n'

        '\nEfeitos: (não)\n'
        'Meio-Ambiente + \n'
        'Economia - \n'
        'População - \n'
          )
          
    decisao18 = input('\nDigite "s" (sim) ou "n" (não): ').lower()
    eventos.remove(evento18)
    while decisao18 not in 'sn' or decisao18 == "":
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

    print_event(
        'MODERNIZAÇÃO DO ENSINO.\n'
        'A secretaria de educação propõe implementar computadores em todas as escolas da rede pública. Deseja aprovar?\n'
        '\nEfeitos: (sim)\n'
        'Economia - \n'
        'Tecnologia + \n'
        'População + \n'

        '\nEfeitos: (não)\n'
        'Economia + \n'
        'Tecnologia - \n'
        'População - \n'
          )
          
    decisao19 = input('\nDigite "s" (sim) ou "n" (não): ').lower()
    eventos.remove(evento19)
    while decisao19 not in 'sn' or decisao19 == "":
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



#inicia a rodada
def rodada():
    global eventos
    eventos = [
    evento1, evento2, evento3, evento4,
    evento6, evento7, evento8, evento9, evento10,
    evento11, evento12, evento13, evento14,
    evento16, evento17, evento18, evento19
    ]

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
            limpar_tela()
            mostrar_interface(pop,eco,meio,tec)
            print('Chuva! A seca finalmente acabou!')
            print('\nAperte Enter para continuar...')
            print(
                '''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣾⣿⣿⣶⣄⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣀⣀⡀⠀⠀⠀
⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀
⠀⢠⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀
⠀⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀
⠀⠈⠿⣿⣿⡿⠋⠈⠻⣿⣿⣿⣿⡿⠟⠁⠀⠙⠿⠿⠛⠁⠙⠻⠿⠿⠟⠁⠀⠀
⠀⠀⠀⠀⣠⡀⠀⠀⢦⡄⠉⠉⣁⠀⠀⠀⠀⠀⠀⠰⡆⠀⠀⢰⣆⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠸⠇⠀⠀⠈⠀⠀⠀⠛⠀⠀⠀⢹⡇⠀⠀⠀⠀⠀⠀⠛⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⡀⠀⠀⢰⡄⠀⠀⣀⠀⠀⠈⠛⠀⠀⢰⣧⠀⠀⠀⣀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠸⣷⠀⠀⠈⠉⠀⠀⢻⡇⠀⠀⠀⡀⠀⠀⠉⠀⠀⠀⢻⡄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠛⠂⠀⠀⢠⡄⠀⠈⠟⠀⠀⠀⢿⠀⠀⠀⣤⠀⠀⠈⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⡀⠀⠀⠃⠀⠀⠀⣀⠀⠀⠘⠃⠀⠀⠉⠀⠀⠀⢰⡄⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠘⠃⠀⠀⠀⠀⠀⠀⠛⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠓⠀⠀
'''
            )
            input()
            tempo_seca -=4
            
        if tempo_hidro == 3:
            limpar_tela()
            mostrar_interface(pop,eco,meio,tec) 
            print('\nO reservatório está cheio novamente! Acabou o racionamento de água!')
            print('\nAperte Enter para continuar...')
            print('''
                       ___
                     .' _ '.
                    / /` `\ \ 
                    | |   [__]
                    | |    {{
                    | |    }}
                 _  | |  _ {{
     ___________<_>_| |_<_>}}____
         .=======^=(___)=^=====.
        / .-------------------. \ 
       / /                     \ \ 
      / /                       \ \ 
     (  '======================='  )
      '---------------------------'
                ''' )
            input()

            tempo_hidro -=3
            
        #mostra a interface do jogo com as barras de indicadores
        mostrar_interface(pop, eco, meio, tec)

        #verifica se o jogador perdeu
        checar_game_over(pop, eco, meio, tec)
        
        #checa se a lista de eventos está vazia antes de escolher um evento aleatório
        if len(eventos) == 0:
            print('Parabéns você sobreviveu ao mandato!\n'
            '\nAperte Enter para voltar ao Menu...')
            input('''
                        .|
                       | |
                       |'|            
               ___    |  |           
       _    .-'   '-. |  |     .--'| 
    .-'|  _.|  |    ||   '-__  |   |  
    |' | |.    |    ||       | |   | 
 ___|  '-'     '    ''       '-'   '-
        ''')
            break

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
    
    Menu()

#introdução do jogo
Menu()
