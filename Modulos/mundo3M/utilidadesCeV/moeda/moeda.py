# def aumentar(preço =0, taxa =0, formato=False):
#     res = preço + (preço * taxa / 100)
#     return res if formato is False else moeda(res)

# def diminuir(preço=0, taxa=0, formato=False):
#     res = preço - (preço * taxa / 100)
#     return res if formato is False else moeda(res)


# def dobro(preço=0, formato=False):
#     res = 2 * preço
#     return res if formato is False else moeda(res)


# def metade(preço=0, formato=False):
#     res = preço / 2
#     return res if formato is False else moeda(res)

# #Exercício 108:

# def moeda(preço=0, moeda='R$'):
#     return f'{moeda}{preço:>.2f}'.replace('.', ',')

#Exercício 109:

#para resolver a confusão {moeda.moeda(moeda.metade(v))} do código principal
# foi inserido o parametro formato=false e a linha de código if formato is False else moeda(res) em cada função

#Exercício 110:

# def resumo(preço=0, taxaa=0, taxar=0, formato=False):
#     print('-'*30)
#     print('RESUMO DO VALOR'.center(30))
#     print('-'*30)
#     print(f'Preço analisado: \t{moeda(preço)}')
#     print(f'Dobro do preço: \t{dobro(preço, True)}')
#     print(f'Metade do Preço: \t{metade(preço, True)}')
#     print(f'{taxaa}% de aumento: \t{aumentar(preço, taxaa, True)}')
#     print(f'{taxar}% de desconto: \t{diminuir(preço, taxar, True)}')