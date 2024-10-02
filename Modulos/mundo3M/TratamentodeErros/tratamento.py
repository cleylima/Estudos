#verificando se o site está ativo

# import urllib
# import urllib.error
# import urllib.request

# try: #tenta executar
#     síte = urllib.request.urlopen('https://www.pudim.com')
# except urllib.error.URLError: #se não conseguir
#     print('\033[0;31mO site não está acessível no momento\033[m')
# else: #se conseguir
#     print('\033[0;32mConsegui acessar o site com sucesso!\033[m')

#________________________________________________

#115a: Vamos criar um menu em Python, usando modularização.

from Interface import *
from arquivo import *
from time import sleep


arq = 'cursoemvideo.txt'

if arquivoExiste(arq):
    print('O Arquivo Existe')
else:
    print('Arquivo não existe!')
    criarArquivo(arq)

while True:
    resp = menu(['Ver Pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'Sair do Sistema'])
    if resp == 1:
        lerArquivo(arq)
    elif resp == 2:
            cabeçalho('NOVO CADASTRO')
            nome = str(input('Nome: '))
            idade = leiaInt('Idade: ')
            cadastrar(arq, nome, idade)
    elif resp == 3:
        cabeçalho('\033[0;31mSistema Encerrado!\033[m')
        break
    else:
        print('\033[0;31mERRO! Informe uma opção válida!\033[m')
    sleep(2)