
#int- Número inteiros(todo número sem vírgula)
#float- Número reais(com vírgula)
#bool- Valores lógicos ou booleanos (True/False)
#str- Caracteres, palavras
#-------------------------------------------------------------------------------

#nome = input('Digite seu nome:')
#print('É um prazer te conhecer {}!' .format (nome))
#-------------------------------------------------------------------------------

#programa que leia dois números e mostre a soma entre eles

n1 = int(input('Informe um número: '))
n2 = int(input('Informe outro número: '))

print(f'A soma de {n1} + {n2} é {n1+n2}')
#-------------------------------------------------------------------------------

#Antecessor e sucessor

#n=int(input('digite um número: '))
#print(f'O antecessor de {n} é {n-1} e o sucessor é {n+1}' )
#-------------------------------------------------------------------------------

#Dobro, triplo e Raiz quadrada

#n=int(input('Digite um numero: '))
#print(f' O dobro de {n} é: {n*2} \n seu triplo é: {n*3} \n e sua raiz quadrada é: {n**(1/2)}') 
#-------------------------------------------------------------------------------

#Calculando média

#n1 = float(input('digite um número: '))
#n2 = float(input('digite um número: '))

#print(f'A média entre {n1} e {n2} é {(n1+n2)/2:.1f}')
#-------------------------------------------------------------------------------

#Conversão de distâncias

#m =float(input('Digite um número: '))
#km = m/1000
#hm = m/100
#dam = m/10
#dm = m*10
#cm = m*100
#mm = m*1000

#print(f' A medida de {m} é igual a: \n {m/1000}km \n {m/100}hm \n {m/10}dam \n {10*m}dm \n {100*m}cm \n {1000*m}mm')
#-------------------------------------------------------------------------------

#Tabuada

#num=int(input('Digite um número para ver sua tabuada: '))

#print('-'*15)
#print(' {} x {:2} = {}'. format(num, 1, num*1))
#print(' {} x {:2} = {}'. format(num, 2, num*2))
#print(' {} x {:2} = {}'. format(num, 3, num*3))
#print(' {} x {:2} = {}'. format(num, 4, num*4))
#print(' {} x {:2} = {}'. format(num, 5, num*5))
#print(' {} x {:2} = {}'. format(num, 6, num*6))
#print(' {} x {:2} = {}'. format(num, 7, num*7))
#print(' {} x {:2} = {}'. format(num, 8, num*8))
#print(' {} x {:2} = {}'. format(num, 9, num*9))
#print(' {} x {:2} = {}'. format(num, 10, num*10))
#print('-'*15)
#-------------------------------------------------------------------------------

#Conversão de real em dólar

#R= float(input('Qual valor deseja converter?: R$'))

#print(f'R$ {R:.2f} equivale a {(R/5.03):.2f} dólares')
#-------------------------------------------------------------------------------

#Pintando parede

#alt = float(input('Altura da parede: '))
#larg= float(input('Largura da parede: '))
#print(f'A Área da sua parede é {alt*larg}m² e precisará de {(alt*larg)/2}l para pintar a parede')
#-------------------------------------------------------------------------------

#Calculando descontos

#p= float(input('qual o valor do produto?: R$ '))
#d= float(input('qual o vaor do desconto? '))
#promo = p - (p*d/100)

#print(f'O produto que custava R${p} com desconto de {d}% custrará R${promo}')
#-------------------------------------------------------------------------------

#Aumento Salarial

#S = float(input('Qual seu salário? R$'))
#A = float(input('Em quanto foi o aumento? '))
#NS = S + (S*A/100)

#print(f'Seu novo salário será de {NS}')
#-------------------------------------------------------------------------------

#Conversão de C° em F°

#C = float(input('Informe o valor da temperatura em °C: '))
#F = ((9*C/5)+32)

#print(f'{C}°C corresponde a {F}°F')
#-------------------------------------------------------------------------------

#Aluguel de Carros

#d = int(input('Por quantos dias o carro foi alugado?: '))
#km = float(input('Quantos quilômetros foram percorridos?: '))

#print(f'O total a pagar é de {d*60 + km*0.15:.2f}R$')
#__________________________________________________________

#Analise:
    #len = (saber o comprimento da sting)
    #count = (contar quantas vezes aparece a letra)
    #find = (Em que momento começa letra/palavra dentro da string)
#Tranformação:
    #replace() = Transformar/Substituir (Substituir uma frase ou letra dentro da string)
    #upper() = (Transforma as letras em minúsculo para maiusculo)
    #lower() = (Transforma letras maiúsculas em minúsculas)
    #capitalize() = (Transforma todas as letras em minúsculo deixando a primeira em maíusculo)
    #title() = (Transforma todas as letras em minúsculo deixando a primeira de cada plavra em maíusculo)
    #strip() = (Remove os espaços indesejados no início e no final da string)
        #PS: Utilizar r no início da strip faz com que a açaõ seja realizada apenas no fim da string, se utilizar l fará a ação ser realizada no começo da string
#Divisão
    #split() = (Divide a string por palavras, transformando-a em várias strings )
#Junção
    #join() = (Junta a string novamnete em uma só)

#022: Crie um programa que leia o nome completo de uma pessoa e mostre: - O nome com todas as letras maiúsculas e minúsculas. - Quantas letras ao todo (sem considerar espaços). - Quantas letras tem o primeiro nome.

    #nome=(str(input('Qual seu nome?: ')))
    #print(nome.upper())
#_________________________________________________________________
    #nome=(str(input('Qual seu nome?: ')))
    #print(nome.lower())

#023: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

    #num = int(input('Digite um número entre 0 e 9999: '))
    #n = str(num)
    #print(f'segue separação do número {n}')
    #print(f'Unidade: {n[0]}')
    #print(f'Dezena: {n[1]}')
    #print(f'Centena: {n[2]}')
    #print(f'Milhar: {n[3]}')

#024: Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

    #city = input('Digite o nome da cidade: ').strip()
    #print(city[:5].upper()=='SANTO')



#025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

    #nome = str(input('Qual seu nome? ').strip())
    #print('O nome tem Silva?: {}'.format('SILVA' in nome.upper()))

#026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

    #name = str(input('Qual seu nome completo? ').upper())
    #print('A letra A aparece {} vezes na frase'.format(name.count('A')))
    #print('A letra A aparece pela rimeria vez na posição {}'.format(name.find('A')))
    #print('A letra A aparece pela ultima fez na posição {}'.format(name.rfind('A')))


#027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

    #name = str(input('Qual seu nome completo? '))
    #nome = name.split()
    #print('seu primeiro nome é {}'.format(nome[0]))
    #print('seu último nome é {}'.format(nome[len(nome)-1]))
#__________________________________________________________________________________

# if e else

#tempo = int(input('Quantos anos você tem?: '))

#if tempo >= 60:
    #print('velho')
#else:
    #print('novo')

#_______________________________________
#n1 = float(input('Digite a primeira nota: '))
#n2 = float(input('Digite a segunda nota: '))
#m = ((n1+n2)/2)
#if m>=7:
    #print('Parabéns')
#else:
    #print('Reprovado')
#print(m)
#_______________________________________

#Jogo da Advinhação

#from random import randint

#computer = randint(0, 5) #faz o programa sortear um número
#print('-=-' * 20)
#print ('Vou pensar em um número de 0 à 5, advinhe qual hehehe ')
#print ('-=-' * 20)
#player = int(input('Qual foi o número?: '))

#if player == computer:
    #print('Acertou, miseravii')
#else:
    #print('Errou, burro, burro, burro!')
    #print(f'Eu pensei no número {computer}, idiota!')

#___________________________________________________________

#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
#vel = int(input('A qual velocidade está dirigindo?: '))
#if vel > 80:
    #print('\033[0;31;40mVocê foi multado por ultrapassar a velocidade minima permitida de 80Km/h')
    #print(f'O valor da multa é de {(vel-80)*7:.2f}R$ \033[m')

#print('Boa Viagem e Dirija com Cuidado!')

#_______________________________________________________

#Descobrir e o número é ímpar ou par

#num = int(input('Digite um número: '))
#valor = num % 2
#if valor == 0:
    #print(f'O número {num} é PAR!')
#else:
    #print(f'O número {num} é ÍMPAR!')
#___________________________________________________

#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

#dist = float(input('Qual a distância que irá percorrer?: '))
#print(f'Você irá realizar uma viagem de {dist}km')
#if dist <= 200:
   # v = dist*0.50

#else:
 #   v= dist*0.45
#print(f'O valor da passagem será de R${v:.2f}')

#________________________________________________________

#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

#from datetime import date
#ano = int(input('Qual ano deseja verifica? Insira 0 para verificar o ano atual: '))

#if ano == 0:
    #ano = date.today().year
#if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    #print(f'O ano {ano} é Bissexto!')
#else:
    #print(f'O ano {ano} não é Bissexto!')

#__________________________________________________________________

#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

#n1 = int(input('Digite o primeiro valor: '))
#n2 = int(input('Digite o segundo valor: '))
#n3 = int(input('Digite o terceiro valor: '))

##if n2<n1 and n2<n3:
    #menor = n2
#if n3<n1 and n3<n1:
    #menor = n3

#maior = n1
#if n2>n1 and n2>n3:
    #maior = n2
#if n3>n1 and n3>n2:
   #maior = n3

#print(f'O maior valor é: {maior} e o menor valor é: {menor}')
#__________________________________________________________
    
#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

#salario = float(input('Qual o salário do funcionário?: '))

#if salario > 1250:
    #Salario = salario + (salario*10/100)
#else:
    #Salario = salario + (salario*15/100)
#print(f'O novo salário será de R${Salario:.2f}, houve um aumento de {Salario - salario:.2f} ')
#________________________________________________________________________________

#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
#a = float(input('Qual o valor do primeiro segmento?: '))
#b = float(input('Qual o valor do segundo segmento?: '))
#c = float(input('Qual o valor do terceiro segmento?: '))

#if b+c>a and a+c>b and b+a>c:
    #print('\033[0;32;40mEstes segmentos podem formar um triângulo!\33[m')
#else:
    #print('\033[0;31;40mEstes segmentos não formam um triângulo!\33[m')
    