from Interface import *

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):

    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso')

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('\033[0;31mERRO AO LER ARQUIVO\033[m')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()

def cadastrar(arq, nome='Desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('\033[0;31mOuve um ERRO na abertura do arquivo!\033[m')
    else:
        try:
            a.write(f'{nome}; {idade}\n')
        except:
            print('\033[0;31mHouve um ERRO na hora de escrever os dados\033[m')
        else:
            print(f'\033[0;32mNovo registro de {nome} cadastrado com SUCESSO!\033[m')
            a.close()