def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Informe um número inteiro válido!\033[m')
            continue
        except(KeyboardInterrupt):
            print('\n\031[31mUsuário preferiu não digitar este número\033[m')
            return 0
        else:
            return n


def linha(tam=42):
    return '-' * tam

def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabeçalho('\033[0;32mMENU PRINCIPAL v1.0\033[m')
    c=1
    for item in lista:
        print(f'\033[0;33m{c}\033[m - \033[0;36m{item}\033[m')
        c+=1
    print(linha())
    opc = leiaInt('Sua Opção: ')
    return opc