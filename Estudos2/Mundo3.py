# VARIÁVEIS COMPOSTAS - TUPLAS /LISTAS / DICIONÁRIOS

#lanche = 'hamburguer', 'suco', 'pizza', 'pudim'
#for cont in range (0, len(lanche)):
    #rint(f'Eu comi {lanche[cont]}')
#print('To cheio')

#ou:

#for comida in lanche:
    #print(f'eu comi {comida}')
#print('To cheio!')
#____________________________________________________

#72: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

#cont = 'Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte'
#while True:
#     num = int(input('Infomre um número entre 0 e 20: '))
#     if 0 <= num <= 20:
#         break
#     print('Tente novamente',end='')
# print(f'O número {num} por extenso é {cont[num]}')
    
#_____________________________________________________________________

#73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética. 
#d) Em que posição está o time do Corinthians.

# time = ('Flamengo', 'Internacional', 'Coritiba', 'Vasco', 'Palmeiras', 'Cuiaba', 'Botafogo', 'Grêmio', 'Bahia', 'Atletico MG', 'Athletico PR', 'Criciuma', 'Bragantino', 'Corinthians')
# print('-='*15)
# print(f'Os 5 primeiros times são {time[:5]}')
# print('-='*15)
# print(f'Os 4 últimos times são {time[-4:]}')
# print('-='*15)
# print(f'Os times em orgem afabética: {sorted(time)}')
# print('-='*15)
# print(f'O time do Corinthias esta na {time.index("Corinthians")+1}ª posição')

#_____________________________________________________________________

#074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

# from random import randint

# numero = (randint(0,10)), randint(0,10), randint(0,10), randint(0,10), (randint(0,10))
# print(f' Os números sorteados foram: {numero}')
# print(f'O maior número foi {max(numero)}')
# print(f'O menor número foi {min(numero)}')

#_________________________________________________________________________

# 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.


# numero = (int(input('Informe um número: ')), int(input('Informe outro número: ')), int(input('Informe mais um número: ')), int(input('Informe o último número: ')))
# print(f'Você digitou os números {numero}')
# print(f'o numero 9 apareceu {numero.count(9)} vezes')
# if 3 in numero:
#     print(f'O número 3 apareceu na {numero.index(3)+1}ª posicão')
# else:
#     print('Não foi informado número 3')
# print('Os valores Pares informados foram: ', end= '')
# for n in numero:
#     if n % 2 == 0:
#         print(n, end= ' ')

#__________________________________________________________________

#6: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular

# list = ('lápis', 1.75, 'caneta', 2.00, 'caderno', 35.50, 'bolsa', 90.00)
# print('-'*40)
# print(f'{"LISTAGEM DE PREÇOS":^40}')
# print('-'*40)
# for pos in range(0, len(list)):
#     if pos % 2 == 0:
#         print(f'{list[pos]:.<30}', end= '')
#     else:
#         print(f'R${list[pos]:>7.2f}')
    
# print('-'*40)

#______________________________________________________________
#Listas

#valores = [3, 2, 5, 9, 7]
#valores.append(9)
#del(valores[2])
#valores[2] = 6
#valores.sort()
#valores.insert(2, 2)
#valores.pop(0)
#valores.reverse()
#print (valores)
#if 1 in valores:
    #valores.remove(5)
#else:
    #print('Não há numero 1 na lista')
#print(f'Esta lista possui {len(valores)} elementos')

#_______________________________________________________________________________

#lista = []
#lista.append(2)
#lista.append(4)
#lista.append(5)
#for cont in range(1, 5):
    #lista.append(int(input('Digite um valor: ')))

#for c, v in enumerate(lista):
    #print (f'na posição {c} encontrei o valor {v}')

#__________________________________________

#78: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. 
#lista = []
#maior = 0
#menor = 0
#for c in range(0, 5):
    #lista.append(int(input(f'Informe um valor para a posiçao {c}: ')))
    #if c == 0:
        #maior = menor = lista[c] 
    #else:
        #if lista[c] > maior:
            #maior = lista[c]
        #if lista[c] < menor:
            #menor = lista[c]

#print(f'Você informou os valores {lista}')
#print(f'O Menor valor informado foi o {menor} na posição ', end='')
#for i, v in enumerate(lista):
    #if v == maior:
        #print(f'{i}...', end='')
#print()
#print(f'E o Maior valor informado foi o {maior} na posição ', end='')
#for i, v in enumerate(lista):
    #if v == menor:
        #print(f'{i}...', end='')
#print()

#_______________________________________________________________________
#79: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente. 

# numeros = []

# while True:
#     valor = int(input('Informe um valor: '))
#     if valor not in numeros:
#         numeros.append(valor)
#         print('Valor adicionado com sucesso')
#     else: 
#         print('Numero repetido, não irei adicionar!')
#     resp = ' '
#     while resp not in 'SN':
#         resp = str(input('Deseja informar outro número?[S/N]: ')).strip().upper()[0]
#     if resp == 'N':
#             break
# print(f'Você informou os números {numeros}')



#_________________________________________________________________________

#80: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela
# numeros = list()

# for c in range(0,5):
#     lista = int(input(f'Informe um número: '))
#     if c == 0 or lista > numeros[-1]:
#         numeros.append(lista)
#         print(f'Numero {lista} adicionado no final da lista')
#     else:
#         pos = 0
#         while pos < len(numeros):
#             if lista <= numeros[pos]:
#                 numeros.insert(pos, lista)
#                 print(f'Numero {lista} inserido na posição {pos}')
#                 break
#             pos += 1
#_____________________________________________________________________________

# print(f'Números informados: {numeros}')

#81: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

# lista = []

# while True: 
#     numeros = int(input('Informe um número: '))
#     if numeros not in lista:
#         lista.append(numeros)
#         print('Número adicionado a lista com sucesso')
#     else:
#         print('Número repetido, não será adicionado')

#     resp = ' '
#     while resp not in 'SN':
#         resp = str(input('Deseja inserir outro número?[S/N]: ')).strip().upper()[0]
#     if resp == 'N':
#         break

# lista.sort(reverse=True)
# print(f'Você informou {len(lista)} números')
# print(f'Em forma decrescente: {lista}')
# if 5 in lista:
#     print('O número 5 se encontra na lista!')
# else:
#     print('O número 5 não foi adicionado a lista')

#_____________________________________________________

#82: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

# lista = []
# listapar = []
# listaimp = []

# while True:
#     numero = int(input('Informe um número: '))
#     lista.append(numero)
#     if numero % 2 == 0:
#         listapar.append(numero)
#     elif numero % 2 == 1:
#         listaimp.append(numero)
#     resp = ' '
#     while resp not in 'SN':
#         resp = str(input('Deseja continuar?[S/N]: ')).strip().upper()[0]
#     if resp == 'N':
#         break
# print(f'Você informou os números {lista}')
# print(f'Os números Pares são: {listapar}')
# print(f'Os números Impares são: {listaimp}')

#_____________________________________________________

#83: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

# expr = str(input('Digite a expressão: '))
# if expr.count('(') == expr.count(')'):
#     print('Sua expressão é válida!!')
# else:
#     print('Sua expressão não é válida')

# ______________________________________________________________

#84: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

# temp = []
# princ = []
# maior = menor = 0

# while True:
#     temp.append(str(input('Informe o nome: ')))
#     temp.append(float(input('Informe o peso: ')))
    
#     if len(princ) == 0:
#         maior = menor = temp[1]
#     if temp[1] > maior:
#         maior = temp[1]
#     if temp[1] < menor:
#         menor = temp[1]

#     princ.append(temp[:])
#     temp.clear()

#     resp = ' '
#     while resp not in 'SN':
#         resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
#     if resp == 'N':
#         break

# print(f'Foram registrados {len(princ)} pessoas')
# print(f'O maior peso foi de {maior}kg. Peso de: ', end='')
# for p in princ:
#     if p[1] == maior:
#         print(f'[{p[0]}] ',end='')
# print()
# print(f'O menor peso foi de {menor}kg. Peso de: ', end='')
# for p in princ:
#     if p[1] == menor:
#         print(f'[{p[0]}] ',end='')
# print()

#_______________________________________________________________________

#85: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

# num = [[], []]
# valor = 0

# for c in range (1,8):
#     valor = int(input(f'Informe o {c}° número: '))
#     if valor % 2 == 0:
#         num[0].append(valor)
#     else:
#         num[1].append(valor)


# num[0].sort()
# num[1].sort()
# print(f'Os números Pares são: {num[0]}; e os números Ímpares são: {num[1]}')

#__________________________________________

#86: Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

# matriz = [[0,0,0],[0,0,0],[0,0,0]]

# for l in range (0,3):
#     for c in range (0,3):
#         matriz[l] [c] = int(input(f'Informe um número para {[l, c]}: '))
# for l in range (0,3):
#     for c in range (0,3):
#         print(f'[{matriz[l] [c]:^5}]', end='')
#     print()

#______________________________________________

#87: Aprimore o desafio anterior, mostrando no final: 
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

# matriz = [[0,0,0], [0,0,0], [0,0,0]]

# spar = scol = mai2 = 0

# for l in range (0,3):
#     for c in range (0,3):
#         matriz[l] [c] = int(input(f'Informe um valor para {[l, c]}: '))
# print('-='*30)
# for l in range (0,3):
#     for c in range(0,3):
#         print(f'[{matriz [l] [c]:^5}]', end= '')
#         if matriz [l] [c] % 2 == 0:
#             spar += matriz [l] [c]
#     print()
# print('-='*30)
# print(f'A soma dos valores pares é {spar}')
# for l in range (0,3):
#     scol+= matriz [l] [2]
# print(f'A soma dos valores da terceira coluna é {scol}')
# for c in range (0,3):
#     if c == 0:
#         mai2 = matriz [1] [c]
#     elif matriz [1] [c] > mai2:
#         mai2 = matriz [1] [c]
# print(f'O maior valor da segunda linha é {mai2}')

#_________________________________________________________

#88: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

# from random import randint

# lista = []
# jogos = []

# print('=-'*30)
# print('=-'*3, 'MEGA SENA', '-='*3)
# print('=-'*30)
# quantidade = int(input('Quantos números deseja sortear?: '))
# total = 1
# while total <= quantidade:
#     cont = 0
#     while True:
#             num = randint(1,60)
#             if num not in lista:
#                 lista.append(num)
#                 cont+=1
#             if cont >= 6:
#                 break
#     lista.sort()           
#     jogos.append(lista[:])
#     lista.clear()
#     total +=1
# print(f'Os {quantidade} palpites da sorte são: ')
# print('')
# for i, l in enumerate(jogos):
#     print(f'Jogo {i+1}: {l}')
# print('')
# print('=-'*3,'BOA SORTE', '-='*3)

#___________________________________________

#89: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente

# lista = []

# while True:
#     nome = str(input('Aluno: '))
#     nota1 = float(input('1ª Nota: '))
#     nota2 = float(input('2ª Nota: '))
#     nota3 = float(input('3ª Nota: '))
#     media = (nota1 + nota2 + nota3) / 3
    
#     lista.append([nome, [nota1, nota2, nota3], media])
#     resp = ' '
#     while resp not in 'SN':
#         resp = str(input('Deseja cadastrar outro aluno?[S/N]: ')).strip().upper()[0]
#     if resp == 'N':
#         break


# for i, a in enumerate(lista):
#     print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
#     print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

# while True:
#     opc=int(input('Deseja verificar as notas de qual aluno?(PS: Informe 999 para encerrar): '))
#     if opc <= len(lista) - 1:
#         print(f'As Notas do {lista[opc][0]} são: {lista[opc][1]}')
#     if opc == 999:
#         break
# print('FINALIZANDO...')

#____________________________________________________________

#Dicionários

# pessoa = {'nome': 'cleyson', 'idade': '22', 'sexo:': 'M'}
#print(f'O {pessoa['nome']} tem {pessoa['idade']} anos')
#print(pessoa.values())
#print(pessoa.items())
#print(pessoa.keys())

# for k in pessoa.keys():
#     print(k)

# for k in pessoa.values():
#     print(k)

# for k, v in pessoa.items():
#     print(f'{k} = {v}')

# pessoa['nome'] = 'Anderson' #substitui o valor do item nome
#del pessoa['sexo'] # delete o item Sexo
#pessoa['peso'] = '67.8' #Adiciona item na variável


#CRIANDO DICIONÁRIO DENTRO DE UMA LISTA:
# Brasil = []
# estado = {'uf': 'Paraiba', 'capital': 'João Pessoa', 'sigla': 'PB'}
# estado2= {'uf': 'São Paulo', 'capital': 'São Paulo', 'sigla': 'SP'}
# Brasil.append(estado)
# Brasil.append(estado2)

# print(Brasil[1]['sigla'])

# estado = {}
# brasil = []
# for c in range (0,3):
#     estado['uf'] = str(input('Informe a UF do estado: '))
#     estado['Sigla'] = str(input('Informe a sigla do estado: '))
#     #brasil.append(estado) # Desta forma o print mostra o ultimo dado informado 3 vezes, ivés dos 3 dados solicitados no input
#     brasil.append(estado.copy())
# #print(brasil)

# for e in brasil:
#     for v in e.values():
#         print(v, end=' = ')
#     print('')

#_____________________________________________________________________
#90: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

# aluno = {}

# aluno['nome'] = str(input('Aluno: '))
# aluno['media'] = float(input('Média do aluno: '))

# if aluno['media'] < 4.0:
#     aluno['situacao'] = 'Reprovado'

# elif aluno['media'] < 7.0:
#     aluno['situacao'] = 'Recuperação'
# else:
#     aluno['situacao'] = 'Aprovado'

# for i, v in aluno.items():
#     print(f'{i}: {v}')

#_______________________________________________

#91: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

# from random import randint
# from time import sleep
# from operator import itemgetter #Pôr o dicionário em ordem

# players = {
#             'Cleyson': randint(1,6),
#             'Juliene': randint(1,6),
#             'Mikaelly': randint(1,6),
#             'Nicoly': randint(1,6)
#             }

# ranking = []

# print('VALORES SORTEADOS')
# for k, v in players.items():
#     print(f'O jogador {k} rolou o dado e caiu: {v}')
#     sleep(0.7)

# print('-='*5, 'RANKING', '=-'*5)


# ranking = sorted(players.items(), key=itemgetter(1), reverse=True) #Colocando o dicinário em ordem 

# for i, v in enumerate(ranking):
#     print(f'Em {i+1}° lugar: {v[0]} com {v[1]} no dado')
#     sleep(0.7)

#__________________________________________________________________

#92: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

# from datetime import datetime
# from time import sleep

# dados={}
# dados['Nome'] = str(input('Informe o nome do profissional: '))
# nasc = int(input('Informe o Ano de Nascimento: '))
# dados['Idade'] = datetime.now().year - nasc
# dados['CTPS'] = int(input('Carteira de Trabalho[0 = não tem]: '))
# if dados['CTPS'] != 0:
#     dados['Ano_de_Contratação'] = int(input('informe o ano de contratação: '))
#     dados['Salario'] = float(input('Informe o salário: R$'))
#     dados['Idade_de_Aposentadoria'] = dados['Idade'] + dados['Ano_de_Contratação'] + 35 - datetime.now().year
#     print('-='*5, 'CALCULANDO', '-='*5)
#     sleep(0.7)
    
#     for k, v in dados.items():
#         print(f'{k}: {v}')
#         sleep(0.7)


# if dados['CTPS'] == 0:
#     for k, v in dados.items():
#         print(f'{k}: {v}')

#_______________________________________________________________________________

#93: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

# Jogador = {}
# gols = []
# Jogador['Nome'] = str(input('Informe o nome do jogador: '))
# Jogador['Partidas_Disputadas'] = int(input(f'Quantas partidas o jogador {Jogador['Nome']} jogou?: '))

# if Jogador['Partidas_Disputadas'] == 0:
#     for k, v in Jogador.items():
#         print(f'{k}: {v}')

# for c in range (1, (Jogador['Partidas_Disputadas']+1)):
#     gls = int(input(f'Gols feitos na {c}° partida: '))
#     gols.append(gls)

#     Jogador['Gols_Marcados'] = gols
#     Jogador['Saldo'] = sum(gols)

# print('-='*30)
# print(Jogador)
# print('-='*30)
# for k, v in Jogador.items():
#     print(f'O campo {k} tem o valor {v}')

# print('-='*30)
# print(f'O jogador {Jogador["Nome"]} jogou {Jogador["Partidas_Disputadas"]}:')
# for i, v in enumerate(Jogador['Gols_Marcados']):
#     print(f'Na partida {i} fez um total de {v} gols')
# print(f'Foi um total de {Jogador["Saldo"]} gols')

#__________________________________________

#94: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

# Pessoas = []
# dicionario = {}
# anos = []
# contM = []
# IdadeAM = []

# while True:
#     dicionario['Nome'] = str(input('Informe o nome: '))
#     dicionario['sexo'] = ' '
#     while dicionario['sexo'] not in 'MF':
#         dicionario['sexo'] = str(input('Informe o Sexo da Pessoa[M/F]: ')).strip().upper()[0]
#     idade = int(input('Informe a idade: '))
#     anos.append(idade)
#     dicionario['Idade'] = idade
#     Pessoas.append(dicionario.copy())

# #Média de Idade

#     media = (sum(anos)) / len(Pessoas)

# #Lista de Mulheres 
#     if dicionario['sexo'] == 'F':
#         contM.append(dicionario['Nome'])

# #Lista de Pessoas Acima da Média
#     if dicionario['Idade'] >= media:
#         IdadeAM.append(dicionario['Nome'])

#     resp = ' '
#     while resp not in 'SN':
    
#         resp = str(input('Deseja continuar?[S/N]: ')).strip().upper()[0]
#     if resp == 'N':
#         break


# print(f'Ao todo foram cadastradas {len(Pessoas)} pessoas')
# print(f'A média de idade das pessoas é de {media}')
# print(f'As mulheres cadastradas foram: {contM}')
# print(f'As pessoas com Idade acima da média são: {IdadeAM}')

#___________________________________________________

#095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

# jogadores = ()
# dados = {}
# gols = ()
# while True:
#     dados['Nome'] = input('\033[1;97mNome do(a) jogador(a): ').strip().title()
#     partidas = int(input(f'Quantas patidas {dados["Nome"]} jogou? '))
#     for p in range(partidas):
#         gols.append(int(input(f'Quantos gols marcou na {p+1}° partida? ')))
#     dados['Gols'] = gols[:]
#     dados['Total'] = sum(gols)
#     jogadores.append(dados.copy())
#     dados.clear()
#     gols.clear()
#     while True:
#         continuar = input('\033[1;97mQuer continuar [S/N]? ').upper().strip()
#         if continuar == 'S' or continuar == 'N':
#             break
#         print('\033[1;31mRESPOSTA INVÁLIDA!')
#     print(60*'\033[1;97m-')
#     if continuar == 'N':
#         print('\033[1;32mJOGADORES CADASTRADOS'.center(60))
#         c = 0
#         for jogador in jogadores:
#             c += 1
#             espaco = 12 - len(jogador["Nome"])
#             print(f'\033[1;97mN°{c}   Nome: {jogador["Nome"]}', end=espaco*' ')
#             print(f'Gols: {jogador["Gols"]}', end=espaco*' ')
#             print(f'Total: {jogador["Total"]}')
#         break
# while True:
#     mostrar = int(input('\033[1;97mMostrar dados de qual jogador (digite 999 p/ encerrar)? '))
#     if mostrar == 999:
#         print('\033[1;33m==================>PROGRAMA ENCERRADO<======================')
#         break
#     elif mostrar > len(jogadores) or mostrar <= 0:
#         print('\033[1;31mRESPOSTA INVÁLIDA!')
#     else:
#         print(60 * '\033[1;97m-')
#         print('\033[1;34m ', end='')
#         print(f'=====>LEVANTAMENTO DO JOGADOR(A) {jogadores[mostrar-1]["Nome"]}<====='.upper())
#         for jogador in jogadores:
#             if jogador == jogadores[mostrar-1]:
#                 for p, gol in enumerate(jogador['Gols']):
#                     print(f'\033[1;97mNo {p + 1}° jogo fez {gol} gol(s)')
#     print(60*'\033[1;97m-')

