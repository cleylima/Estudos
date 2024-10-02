# Estrutura de repetição for

#46: Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
#from time import sleep

#for c in range(10,-1,-1):
  #  sleep (1)
  #  print (c)
#sleep (0.5)
#print ('CABUUUUUUM')

#_____________________________________________

#047: Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

#for par in range (2,51,2):
 #   print (par)
#print('FIM')

#________________________________________________

#48: Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
#soma = 0
#cont = 0
#for m in range (1,501, 2):
    #if m %3 == 0:
    #    soma = soma + m
    #    cont = cont + 1
#print (f' A soma de todos os {cont} números múltiplos por 3 é {soma}')

#______________________________________________________

#Tabuada

#num=int(input('Digite um número para ver sua tabuada: '))

#for c in range (0,11):
  #print(' {} x {:2} = {}'. format(num, c, num*c))

#_______________________________________________________________

 #050: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

#s = 0
#cont = 0

#for c in range (1,7):
  #  num = int(input('Digite um número: '))
  #  if num % 2 == 0:
  #      s += num 
  #      cont += 1
#print(f' você informou {cont} números PARES e a soma deles é {s}')

#____________________________________________________________________

#51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão

#term = int(input('Digite um número: '))
#raz = int(input('Digite o valor da razão: '))
#dec = term + (10-1) * raz

#for c in range (term, dec + raz, raz ):
   #print (f'{c}', end= " -> ")
#print('Acabou')

#_______________________________________________________________________

#52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

#num = int(input('Digite um número: '))
#tot = 0
#for c in range (1, num +1): 
  #if num % c == 0:
    #print('\033[33m', end=' ')
    #tot+=1
  #else:
    #print('\033[31m', end=' ')
  #print(f'{c}',end=' ')
#print(f'\n\033[mO número {num} foi divisível {tot} vezes')
#if tot == 2:
  #print('E por isso ele é um número primo')
#else:
  #print('E por isso ele não é um número primo')

#__________________________________________________________________

#57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

#sexo = str(input('Informe o Sexo [M/F]: ')).strip().upper()[0]
#while sexo not in 'FM':
  #sexo = str(input('Informação inválida! Informa seu sexo [M/F]: ')).strip().upper()[0]
#print(f'Sexo {sexo} registrado com sucesso')

#_________________________________________________________________


#58: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

#from random import randint
#cont = 0
#computer = randint(0, 10) #faz o programa sortear um número
#print('-=-' * 20)
#print ('Vou pensar em um número de 0 à 10, advinhe qual hehehe ')
#print ('-=-' * 20)
#acertou = False

#while not acertou:
    #player = int(input('Qual foi o número?: '))
    #cont += 1
    #if player == computer:
      #acertou = True
    #else:
       #if player < computer:
          #print('Tente um valor maior...')
       #elif player > computer:
         # print('Tente um valor menor...')
#print(f'Acertou, miseravii!! Você acertou após {cont} tentativas')

#________________________________________________________________________

#59: Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.

#valor1 = float(input('Insira o primeiro valor: '))
#valor2 = float(input('Insira o segundo valor: '))
#ação = 0
#while ação != 5:
  #print ('-=-' * 20)
  #print('''O que deseja fazer com estes valores?: 
      #[ 1 ] somar
      #[ 2 ] multiplicar
      #[ 3 ] maior
      #[ 4 ] novos números
      #[ 5 ] sair do programa
     # ''')
  #ação = int(input('Informe sua escolha: '))
  #print ('-=-' * 20)

  #if ação == 1:
    #print(f'A soma entre {valor1} e {valor2} é {valor1 + valor2}')
  #elif ação == 2:
    #print(f'A multimplicação entre {valor1} e {valor2} é {valor1 * valor2}')
  #elif ação == 3:
    #if valor1 > valor2:
      #print(f'O maior valor informado foi {valor1}')
    #else:
      #print(f'O maior valor informado foi {valor2}')
  #elif ação == 4:
    #print('Informe os números que deseja: ')
    #valor1 = float(input('Insira o primeiro valor: '))
    #valor2 = float(input('Insira o segundo valor: '))
  #elif ação == 5:
    #print('Finalizando...')
  #else:
    #print('Opção Inválida! Tente novamente')
#print('Fim do Programa')

#_____________________________________________________

#60: Faça um programa que leia um número qualquer e mostre o seu fatorial.

#n = int(input('Digite um número: '))
#c = n
#f = 1
#print(f'Calculando {n}! = ', end='')
#while c > 0:
    #print(f'{c}', end='')
    #print(' x ' if c > 1 else ' = ', end='')
    #f *= c
    #c -= 1
#print(f'{f}')

#_____________________________________________________________________
#61: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while

#term = int(input('Digite um número: '))
#raz = int(input('Digite o valor da razão: '))
#termo = term
#cont = 1

#while cont <= 10:
    #print(f'{termo} -> ', end='')
    #termo += raz
    #cont += 1
#print('FIM')

#__________________________________________

#62: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

#term = int(input('Digite um número: '))
#raz = int(input('Digite o valor da razão: '))
#termo = term
#cont = 1
#total = 0
#nv = 10
#while nv != 0:
  #total = total + nv
  #while cont <= total:
      #print(f'{termo} -> ', end='')
      #termo += raz
      #cont += 1
      
  #print('PAUSA')
  #nv = int(input('Quantos termos deseja mostrar a mais?: '))
#print(f'Progressão finalizada com {total} termos termos motrados')

#___________________________________________________________________

#63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci

#n = int(input('Quantos termos deseja ver?: '))
#t1 = 0
#t2 = 1
#print(f'{t1} -> {t2}',end='')
#cont = 3
#while cont <= n:
    #t3 = t1 + t2
    #print(f'-> {t3}',end='')
    #t1 = t2
    #t2 = t3
    #cont += 1
#print ('-> FIM')

#_________________________________________________________________________
#4: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)

#n = cont = soma = 0
#n = int(input('Informe um número[999 para parar]: '))
#while n != 999:
    #soma += n
    #cont += 1
    #n = int(input('Informe outro número: '))
#print(f'Você informou {cont} números e a soma deles é {soma}')

#________________________________________________________________________

#65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.


#res = 'S'
#soma = quantidade = media = maior = menor = 0
#while res in 'Ss':
  #num = int(input('Informe um número: '))
  #soma += num
  #quantidade += 1
  #if quantidade == 1:
    #maior = menor = num
  #else:
    #if num > maior:
     # maior = num
    #if num < menor:
     # menor = num

  #res = str(input('Quer continuar?[S/N]: ')).upper().strip()[0]
#media = soma / quantidade 
#print(f'''Você informou {quantidade} de números e a média entre eles é de {media}
#O maior número informado foi {maior} e o menor foi {menor}''')
#print('FIM')

#____________________________________________________

#66: Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

#cont = soma = 0
#while True:
    #n = int(input('Informe um número[999 para parar]: '))
    #if n == 999:
       # break
    #soma += n
    #cont += 1
#print(f'Você informou {cont} números e a soma entre eles é {soma}')

#__________________________________________________

#67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo
#while True:  
  #tab=int(input('De qual número deseja ver a tabuada?: '))
  #if tab < 0:
      #break
  #print('-=-'*10)
  #for c in range(0, 11):
    #print(f' {tab} x {c} = {tab*c}')
  #print('-=-'*10)
    
#print('acabou')

#____________________________________________________

#68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. 

#from random import randint
#v = 0
#while True:
    #player = int(input('Informe um número: '))
    #computador = randint(0, 10)
    #total = player + computador
    #tipo = ' '
    #while tipo not in 'PI':
        #tipo = str(input('Deseja Par ou Ímpar[P/I]?: ')).strip().upper()[0]
    #print(f'Você jogou {player} e o computador {computador}. Total de {total}')
    #if tipo == 'P':
        #if total % 2 == 0:
            #print('VOCÊ VENCEU')
            #v += 1
        #else:
            #print('VOCÊ PERDEU!')
            #break
    #elif tipo == 'I':
        #if total % 2 == 1:
           #print('VOCÊ VENCEU')
           #v += 1
        #else:
            #print('VOCÊ PERDEU!')
            #break
    #print('Vamos jogar novamente...')
#print(f'GAME OVER!!! Você venceu {v} vezes')

#________________________________________________________________

#Programa que questione o produto e o valor e no fim mostre o valor total gasto, quantos produtos custaram mais de 1000 reais e qual o produto mais barato e seu valor

#total = totmil = menor = cont = 0
#barato = ' '

#while True:
    #produto =  str(input('Produto: '))
    #valor = float(input('Valor do Produto: R$'))
    #cont += 1
    #total += valor
    #if valor > 1000:
      #totmil += 1 
    #if cont > 1 or valor < menor:
      #barato = produto
      #menor = valor
    #resp = ' '
    #while resp not in 'SN':
      #resp = str(input('Deseja cadastrar novo produto?[S/N]')).strip().upper()[0]
    #if resp == 'N':
      #break

#print(f'O total gato foi R${total:.2f}')
#print(f'Há {totmil} produto que custou mais de mil reais')
#print(f'O produto mais barato foi {barato} no valor de R${menor}')

#_________________________________________________________

#69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos. 

#cont18 = homem = mul20 = 0
#while True:
    #idade = int(input('Idade: '))
    #if idade > 18:
      #cont18 += 1
    #sexo = ' '
    #while sexo not in 'MF':
      #sexo = str(input('Sexo[M/F]: ')).strip().upper()[0]
    #if sexo == 'M':
        #homem += 1
    #if sexo == 'F' and idade < 20:
        #mul20 += 1
    #resp = ' '
    #while resp not in 'SN':
        #resp = str(input('Deseja continuar?[S/N]')).strip().upper()[0]
    #if resp == 'N':
        #break
#print(f'Forarm cadastradas {cont18} pessoas maiores de 18 anos')
#print(f'Foram cadastrados {homem} homens')
#print(f'Foram cadastradas {mul20} mulheres com menos de 20 anos')

#_____________________________________________________

#71: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
#OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

#valor = int(input('Qual valor deseja sacar? R$'))
#total = valor
#ced = 50
#totced = 0

#while True:
    #if total >= ced:
        #total -= ced
        #totced += 1
    #else:
        #if totced > 0:
            #print(f'Total de {totced} cédulas de R${ced}')
        #if ced == 50:
            #ced = 20
        #elif ced == 20:
            #ced = 10
        #elif ced == 10:
            #ced = 1
       # totced = 0
        #if total == 0:
            #break
    