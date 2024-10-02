#107: Crie um módulo chamado moeda.py que tenha as funções incorporadas  aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.
# from utilidadesCeV.moeda import moeda
# from utilidadesCeV.dado import dado

# v = float(input('Digite o preço: R$'))
# print(f'A metade de {v} é {moeda.metade(v)}')
# print(f'O dobro de {v} é {moeda.dobro(v)}')
# print(f'Aumentando 10% temos: {moeda.aumentar(v, 10)}')
# print(f'Diminuindo 10% temos: {moeda.diminuir(v, 10)}')
 
#____________________________________________

#108: Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.

# v = float(input('Digite o preço: R$'))
# print(f'A metade de {moeda.moeda(v)} é {moeda.moeda(moeda.metade(v))}')
# print(f'O dobro de {moeda.moeda(v)} é {moeda.moeda(moeda.dobro(v))}')
# print(f'Aumentando 10% temos: {moeda.moeda(moeda.aumentar(v, 10))}')
# print(f'Diminuindo 10% temos: {moeda.moeda(moeda.diminuir(v, 10))}')

#______________________________

#109: Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

# v = float(input('Digite o preço: R$'))
# print(f'A metade de {moeda.moeda(v)} é {moeda.metade(v, True)}')
# print(f'O dobro de {moeda.moeda(v)} é {moeda.dobro(v, True)}')
# print(f'Aumentando 10% temos: {moeda.aumentar(v, 10, True)}')
# print(f'Diminuindo 10% temos: {moeda.diminuir(v, 10, True)}')



#________________________________

#110: Adicione ao módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.

# v = float(input('Digite o preço: R$'))
# moeda.resumo(v, 80, 35)

#_____________________________________

#112: Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imput(), mas com uma validação de dados para aceitar apenas valores que sejam monetários.

# v = dado.leiaDinheiro('Digite o preço: R$')
# moeda.resumo(v, 80, 35)