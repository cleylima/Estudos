# def mensagem(txt):
#     print('-'*30)
#     print(txt)
#     print('-'*30)


# mensagem('Olá, Boa Tarde!')
# mensagem('Tudo bem?')

# def soma(a, b):
#     s = a+b
#     print(s)

# soma(3, 2)
# soma(4, 5)
# soma(9, 9)

# def dobra(lst):
#     pos = 0
#     while pos < len(lst):
#         lst[pos] *= 2
#         pos +=1

# valores = [6, 3, 9, 1, 0, 2]
# dobra(valores)
# print(valores)

# def soma(* valores): #usa-se * quando não saber quantos valores serão inseridos
#     s=0
#     for num in valores:
#         s+=num
#     print(f'Somando os valores {valores} temos: {s}')


# soma(5,2)
# soma(1,2,3,4)
# soma(3,5,7,3,5,7,8)

#______________________________________________

#96: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno

# def área(larg, comp):
#     a = larg * comp
#     print(f'A área de um terrono {larg}x{comp} é {a}')

# l = float(input('Largura: '))
# c = float(input('Comprimento: '))

# área(l, c)

#___________________________________________

#97: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

# def escreva(txt):
#     print('~'*len(digite))
#     print(f'{txt}')
#     print('~'*len(digite))

# digite = str(input('Digite uma frase: '))
# escreva(digite)

#_________________________________________________

#98: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:

# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

# from time import sleep

# def contador (i, f, p):
#     if p < 0:
#         p *= -1
#     if p == 0:
#         p = 1
#     print('-='*20)
#     print(f'A contagem de {i} até {f} de {p} em {p}:')
#     sleep(2.5)

#     if i < f:
#         cont = i
#         while cont <= f:
#             print(f'{cont}, ',end='', flush=True)
#             sleep(0.5)
#             cont += p
#         print('FIM!')
#     else:
#         cont = i
#         while cont >= f:
#             print(f'{cont}, ',end='', flush=True)
#             sleep(0.5)
#             cont -= p
#         print('FIM!')



# contador(1, 10, 1)
# contador(10, 0, 2)
# print('-='*20)
# print('Agora é usa vez de personalizar a contagem!')
# ini = int(input('Início: '))
# fim = int(input('Fim: '))
# pas = int(input('Passo: '))
# contador(ini, fim, pas)
# print('Programa Encerrado!')

#_________________________________________

#99: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maio

# from time import sleep

# def maior(*valores):
#     print('='*50)
#     print('Analisando os Valores informados...')
#     sleep(1)
#     m = 0
#     for num in valores:
#         if num > m:
#             m = max(valores)
#     print(f'{valores} foram informados {len(valores)} números ao todo!', flush=True)
#     sleep(0.5)
#     print(f'O maior valor é o {m}')

# maior(1, 3, 5, 2)
# maior(9, 2, 5, 0)
# maior(4, 10, 3, 8, 1)
# maior()

#________________________________________________________________

# 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior

# from random import randint
# from time import sleep

# numeros= []

# def sorteia(num):
#     print('Sorteando 5 valores... ')
#     for c in range (0,5):
#         n = randint(0,10)
#         num.append(n)
#         sleep(0.5)
#         print(f'{n}, ', end='', flush=True)
#         sleep(0.3)


# def somaPar(num):
#     soma = 0
#     for valor in num:
#         if valor % 2 == 0:
#             soma += valor
#     print(f'Somando os valores pares de {num}, temos: {soma}')
    
# sorteia(numeros)
# somaPar(numeros)

#_________________________________
#101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

# def voto(ano):
#     from datetime import datetime
#     ano = datetime.now().year - idade
#     if ano >= 18:
#         print(f'Com {ano} anos: seu voto é obrigatório!')
#     elif ano == 17 or ano == 16 or ano > 60:
#         print(f'Com {ano} anos: seu voto é opcional!')
#     else:
#         print(f'Com {ano} anos: Não Vota!')

# idade = int(input('Informe o ano de nascimento: '))
# voto(idade)

#____________________________________________________

# #102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

# def fatorial(n, show = False):
#     """
#     -> Calcula o fatorial de um número:
#     : Para n: O número a ser calculado
#     : Para Show: (opcional) mostrar ou não a conta
#     : Return: O valor fatorial de um número n 
#     """
#     f = 1
#     for c in range (n, 0, -1):
#         if show:
#             print(c, end='')
#             if c > 1:
#                 print(' x ', end='')
#             else:
#                 print(' = ', end='')
#         f*=c
#     return f



# #print(fatorial(5, show=True))
# help(fatorial)

#_________________________________________

#103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

# def ficha(jog='<desconhecido>', gol=0):
#     print(f'O jogador {jog} fez {gol} Gol(s) no campeonato')


# nome = str(input('Informe o nome do jogador: '))
# gols = str(input('Gols marcados: '))

# if gols.isnumeric():
#     gols = int(gols)
# else:
#     gols = 0
# if nome.strip() == '':
#     ficha(gol=gols)
# else:
#     ficha(nome, gols)

#________________________________

#104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
#Ex: n = leiaInt('Digite um n: ')

# def leiaInt(msg):
#     ok = False
#     valor = 0 
#     while True:
#         n = str(input(msg))
#         if n.isnumeric():
#             valor = int(n)
#             ok = True
#         else:
#             print('\033[0;31mErro! Insira um número inteiro válido!\033[m')
#         if ok:
#             break
#     return valor

# n = leiaInt('Digite um número: ')
# print(f'Você informou o número: {n}')

#____________________________________________

#105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional)

# def notas(*valores, sit=False):
#     r = {}
#     r['total'] = len(valores)
#     r['maior'] = max(valores)
#     r['menor'] = min(valores)
#     r['media'] = sum(valores) / len(valores)
    
#     if sit:
#         if r['media'] <= 6:
#             r['situação'] = 'RUIM'
#         elif r['media'] <= 7:
#             r['situação'] = 'RAZOÁVEL'
#         else:
#             r['situação'] = 'ÓTIMA'
#     return r
    


# resp = notas(5.5, 2.5, 9, 8.5, sit = False)
# print(resp)

#_____________________________________________

#106: Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use cores.

# from time import sleep

# c = ('\033[m',        #0 - Sem cor
#     '\033[0;30;41m',  #1 - Vermelho
#     '\033[0;30;42m',  #2 - Verde
#     '\033[0;30;43m',  #3 - Amarelo
#     '\033[0;30;44m',  #4 - Azul
#     '\033[0;30;45m',  #5 - Roxo
#     '\033[7;30m'     #6 - Branco
#      )

# def ajuda(com):
#     titulo(f'Acessando o manual do comando \'{com}\'', 4)
#     print(c[6], end= '')
#     help(com)
#     print(c[0], end= '')
#     sleep(2)

# def titulo(msg, cor = 0):
#     tam = len(msg) +4
#     print(c[cor], end= '')
#     print('~' *tam)
#     print(f'  {msg}')
#     print('~' *tam)
#     print(c[0], end= '')
#     sleep (1)


# comando = ''
# while True:
#     titulo('SISTEMA DE AUJUDA PYHELP', 2)
#     comando = str(input('Função ou Biblioteca > '))
#     if comando.upper() == 'FIM':
#         break
#     else:
#         ajuda(comando)
# titulo('ATÉ LOGO!', 1)