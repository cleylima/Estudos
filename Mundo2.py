## Condições Aninhadas
# if - elif - else (elif = if+else, forma condição dentro da condição)

#Programa para aprovar o empréstimo bancário para a compra de uma casa. 
#Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 

#valor=float(input('Qual o valor da casa?: R$'))
#salario=float(input('Qual o salário do comprador?: R$'))
#tempo=int(input('Quantos anos de financiamento?: '))
#prestação = valor / (tempo*12)
#minimo = salario * 30/100

#print(f'Para um financimaneto no valor de {valor} ser pago em {tempo} anos, a prestação será de {prestação:.2f}R$')

#A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
#if prestação <= minimo:
    #print('Empréstitmo APROVADO')

#else:
    #print('Empréstimo NEGADO')

#_________________________________________________________________________

#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

#numero = int(input('Digite um numero: '))
#print('''Esolha uma das bases para conversão:
      #[1] BINÁRIO
      #[2] OCTAL
      #[3] HEXADECIMAL''')
#opcao = int(input('Digite sua opção:'))
#if opcao == 1:
    #print(f'{numero} convertdo em BINÁRIO é igual a {bin(numero)[2:]}')
#elif opcao == 2:
    #print(f'{numero} convertido em OCTAL é igual a {oct(numero)[2:]}')
#elif opcao == 3:
    #print(f'{numero} convertido em HEXADECIMAL é igual a {hex(numero)[2:]}')
#else:
    #print('Base esolhida não identificada')

#___________________________________________________________________________

# 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#- O primeiro valor é maior
#- O segundo valor é maior
#- Não existe valor maior, os dois são iguais

#num1 = int(input('Digite um número: '))
#num2 = int(input('Digite outro número: '))

#if num1 > num2:
    #print('O primeiro valor é maior')
#elif num2 > num1:
    #print('O segundo valor é maior')
#else:
    #print('Não existe valor maior, os dois são iguais')

#___________________________________________________________________

# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

#from datetime import date

#atual = date.today().year
#nas = int(input('Ano de Nascimento: '))
#idade = ano - nas
#print(f'Quem nasceu em {nas} possui {idade} anos em {atual}')

#if idade < 18:
    #print(f'Ainda faltam {18-idade} anos para o alistamento ')
    #print(f'Seu alistamento será em {nas+18}')
#elif idade == 18:
    #print('Você deve se alistar IMEDIATAMENTE')
#else:
    #print(f'Você já deveria ter se alistado há {idade-18} anos')
    #print(f'Seu alistamento foi em {nas+18}')

#_________________________________________________________________________

#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#- Média abaixo de 5.0: REPROVADO
#- Média entre 5.0 e 6.9: RECUPERAÇÃO
#- Média 7.0 ou superior: APROVADO

#n1 = float(input('Digite a primeira nota: '))
#n2 = float(input('Digite a segunda nota: '))
#m = (n1+n2)/2

#if m < 5.0:
    #print(f'A média foi {m} abaixo de 5.0: REPROVADO')
#elif 7 > m >= 5.0:
    #print(f'A Média foi {m}: RECUPERAÇÃO')
#else:
    #print(f'A Média foi {m}: APROVADO')

#______________________________________________________________________

#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#- Até 9 anos: MIRIM
#- Até 14 anos: INFANTIL
#- Até 19 anos: JÚNIOR
#- Até 25 anos: SÊNIOR
#- Acima de 25 anos: MASTER

#from datetime import date

#atual = date.today().year

#ano = int(input('Qual o ano de nascimento?: '))
#idade = atual - ano

#if idade <= 9:
    #print(f'{idade} anos: Categoria MIRIM')
#elif idade <= 14:
    #print(f'{idade} anos: Categoria INFANTIL')
#elif idade <= 19:
    #print(f'{idade} anos: Categoria JÚNIOR')
#elif idade <= 25:
   # print(f'{idade} anos: Categoria SÊNIOR')
#else:
    #print(f'{idade} anos: Categoria MASTER')

#______________________________________________________________________________

#042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#- EQUILÁTERO: todos os lados iguais
#- ISÓSCELES: dois lados iguais, um diferente
#- ESCALENO: todos os lados diferentes

#a = float(input('Tamanho do primeiro segmento: '))
#b = float(input('Tamanho do segundo segmento: '))
#c = float(input('Tamanho do terceiro segmento: '))

#if b+c>a and a+c>b and b+a>c:
    #print('\033[0;32;40mEstes segmentos podem formar um triângulo\33[m', end=' ')

    #if a == b == c:
        #print('EQUILÁTERO!')
    #elif a != b != c != a:
        #print('ESCALENO')
    #else:
        #print('ISÓSCELES!')
#else:
    #print('\033[0;31;40mEstes segmentos não formam um triângulo!\33[m') 

#____________________________________________________________

#043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#- IMC abaixo de 18,5: Abaixo do Peso
#- Entre 18,5 e 25: Peso Ideal
#- 25 até 30: Sobrepeso
#- 30 até 40: Obesidade
#- Acima de 40: Obesidade Mórbida

#peso = float(input('Informe o peso: '))
#altura = float(input('Informe a altura: '))
#imc = peso / (altura*altura)

#if imc < 18.5:
    #print(f'O IMC é {imc:.1f}kg/m2: Abaixo do Peso')
#elif imc <= 25:
    #print(f'O IMC é {imc:.1f}kg/m2: Peso Ideal')
#elif imc <= 30:
    #print(f'O IMC é {imc:.1f}kg/m2: Sobrepeso')
#elif imc <= 40:
    #print(f'O IMC é {imc:.1f}kg/m2: Obesidade')
#else:
    #print(f'O IMC é {imc:.1f}kg/m2: Obesidade')

#____________________________________________________________________

 #044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#- à vista dinheiro/cheque: 10% de desconto
#- à vista no cartão: 5% de desconto
#- em até 2x no cartão: preço formal
#- 3x ou mais no cartão: 20% de juros

#valor = float(input('Qual o valor das compras? R$'))
#print('''ESOLHA A FORMA DE PAGAMENTO
    #[1] À vista dinheiro/cheque
    #[2] À vista no cartão
    #[3] Em até 2x no cartão
    #[4] Em 3x ou mais no cartão
    #''')
#opcao = int(input('Como deseja pagar? '))

#if opcao == 1:
   # preco = valor - valor * (10/100)
#elif opcao == 2:
  #  preco = valor - valor * (5/100)
#elif opcao == 3:
    #preco = valor
    #print(f'Sua compra será parcelada em 2x de R${valor / 2} Sem Juros')
          
#else:
    #totalparc = float(input('Irá dividir em quatas vezes?: '))
    #preco = valor + valor * (20/100)
    #parcela = preco / totalparc
    #print(f'Sua compra será parcelada em {totalparc}x de R${parcela} com juros')
    
#print(f'O valor das compras foram de: R${valor:}, o valor a pagar é de R${preco:}')


#_________________________________________________________________________________________

#45: Crie um programa que faça o computador jogar Jokenpô com você

#from random import randint
#itens = ('PEDRA', 'PAPEL', 'TESOURA')
#computador = randint(0, 2)
#print('''FAÇA SUA JOGADA:
    #  [0] PEDRA
    #  [1] PAPEL
    #  [2] TESOURA
    #  ''')
#jogador = (int(input('O que vai jogar?: ')))
#print(f'O Computador jogou: {itens[computador]}')
#print(f'Você jogou: {itens[jogador]}')

#if computador == 0:
    #if jogador == 0:
    #    print('EMPATE! VAMOS NOVAMENTE?')

    #elif jogador == 1:
    #    print('VOCÊ VENCEU! DROGA! VAMOS NOVAMENTE?')

    #elif jogador == 2:
    #    print('EU GANHEI OTÁRIO, HAHA! TENTE NOVAMENTE')

    #else:
    #    print('JOGADA INVÁLIDA')


#elif computador == 1:
    #if jogador == 0:
    #    print('EU GANHEI OTÁRIO, HAHA! TENTE NOVAMENTE ')

    #elif jogador == 1:
    #    print('EMPATE! VAMOS NOVAMENTE?')

    #elif jogador == 2:
    #    print('VOCÊ VENCEU! DROGA! VAMOS NOVAMENTE?')

    #else:
    #    print('JOGADA INVÁLIDA')
#elif computador == 2:
    #if jogador == 0:
    #    print('VOCÊ VENCEU! DROGA! VAMOS NOVAMENTE? ')

    #elif jogador == 1:
    #    print('EU GANHEI OTÁRIO, HAHA! TENTE NOVAMENTE')

    #elif jogador == 2:
    #    print('EMPATE! VAMOS NOVAMENTE?')

    #else:
    #    print('JOGADA INVÁLIDA')
#_________________________________________________________________

#053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços

#frase = str(input('Digite uma frase: ')).strip().upper()
#palavras = frase.split()
#junto = ''.join(palavras)
#inverso = ''
#for letra in range (len(junto)-1,-1,-1):
    #inverso += junto[letra]
#print(f'O inverso de {junto} é {inverso}')
#if inverso == junto:
    #print('Temos um palíndromo!')
#else:
    #print('Não temos um palíndromo')
#___________________________________________________________________________

#054: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

#from datetime import date
#atual = date.today().year
#totmaior = 0
#totmenor = 0

#for pess in range (1, 8):
    #nasc = int(input(f'Em que ano a {pess}ª pessoa nasceu?: '))
    #idade = atual - nasc
    #if idade >= 18: 
       # totmaior += +1
   # else:
      #  totmenor += +1
#print(f'Ao todo temos {totmaior} pessoas maior de idade')
#print(f'E tivemos {totmenor} pessoas menores de idade') 
#________________________________________________________________________

#55: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
#pesmaior = 0
#pesmenor = 0

#for pess in range (1,6):
   # peso = float(input(f'Qual o peso da {pess}ª pessoa?: '))
   # if pess == 1:
    #    pesmaior = peso
    #    pesmenor = peso
    #else:
        #if peso > pesmaior:
          #  pesmaior = peso
       # if peso < pesmenor:
          #  pesmenor = peso
#print(f'O maior peso informado foi {pesmaior}')
#print(f'O menor peso informado foi {pesmenor}')

#___________________________________________________________

#056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

#si = 0
#mi = 0
#mih = 0
#nv = ''
#tm20 = 0
#for p in range (1, 5):
    #print(f'----{p}ª Pessoa----')
    #nome = str(input('Nome: ')).strip()
    #idade = int(input('Idade: '))
    #sexo = str(input('Sexo [M/F]: ')).strip()
    #si += idade

    #if p == 1 and sexo in 'Mm':
        #mih = idade
        #nv = nome
    #if sexo in 'Mm' and idade > mih:
       # mih = idade
       # nv = nome
    #if sexo in 'Ff' and idade < 20:
        #tm20 += +1
#mi = si / 4
#print(f'A média de idade do grupo é {mi}')
#print(f'O homem mais velho se chama {nv} e possui {mih} anos')
#print(f'Ao todo há {tm20} mulheres com menos de 20 anos')

        
    