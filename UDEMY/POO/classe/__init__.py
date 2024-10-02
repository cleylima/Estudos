# class Pessoa:
    # def __init__(self, nome, sobrenome, idade, comendo=False, falando=False):
    #     self.nome=nome
    #     self.sobrenome=sobrenome
    #     self.idade=idade
    #     self.comendo=comendo
    #     self.falando=falando

    # def comer(self, alimento):

    #     if self.comendo:
    #         print(f'{self.nome} já está comendo!')
    #         return

    #     if self.falando:
    #         print(f'{self.nome} está falando, não pode comer agora')
    #         return

    #     return(f'{self.nome} está comendo {alimento}...')
    #     self.comendo = True

    # def Parar_de_Comer(self):
    #     if not self.comendo:
    #         print(f'{self.nome} não está comendo')
    #         return
        
    #     return(f'{self.nome} parou de comer!')
    #     self.comendo=False

    # def falar(self, falando=False):
    #     if self.comendo == True:
    #         print(f'{self.nome} está comendo, não pode falar')
    #         return
        
    #     return(f'{self.nome} está falando')
    #     self.falando = True

    # def Parar_de_Falar(self):
    #     if not self.falando:
    #         print(f'{self.nome} não esta falando')
    #         return
        
    #     return(f'{self.nome} parou de falar!')
    #     self.falando=False

# class Conection:
    # def __init__(self, host='localhost'):
    #     self.host=host
    #     self.pasword=None
    #     self.user=None

    # def set_user(self, user):  #Configura o user declarado na classe
    #     self.user=user

    # def set_pasword(self, pasword): #Configura o pasword declarado na classe
    #     self.pasword=pasword

    # @classmethod #não utiliza self e sim cls que significa classe, desta forma retorna valores atribuidos diretamente na classe e não na função
    # def create_with_auth(cls, user, pasword):
    #     Conection=cls()
    #     Conection.user=user
    #     Conection.pasword=pasword
    #     return Conection


# class Caneta():
#     def __init__(self, cor):
#         self.cor_tinta = cor #Apenas desta forma caso queira mudar o código (cor) para outro nome, terá que mudar em todos os programas que está chamadno este código

#     def get_cor(self):
#         return self.cor_tinta #com isso evita de ter de mudar o código inteiro
    
#     @property
#     def cor(self):

#_______________________________________
#Associação - Associa duas classes porém ambas funcionam perfeitamente separadamente 
# class Escritor:
#     def __init__(self, nome) -> None:
#         self.nome=nome
#         self._ferramenta = None

#     @property
#     def ferramenta(self):        #esta função se chama Getter e é usada apenas para retornar o valor, não configura o parametro '_ferramenta'
#         return self._ferramenta
    
#     @ferramenta.setter
#     def ferramenta(self, ferramenta):        #esta funçaõ se chama setter e configura o parametro _ferramenta
#         self._ferramenta = ferramenta


# class FerramentaDeEscrever:
#     def __init__(self, nome):
#         self.nome=nome

#     def escrever(self):
#         return f'{self.nome} está escrevendo'
    
# escritor = Escritor('Luiz')
# caneta = FerramentaDeEscrever('Caneta BIC')
# maquina_de_escrever = FerramentaDeEscrever('Máquina')
# escritor.ferramenta = maquina_de_escrever  #Associação entre classes


# print(caneta.escrever())
# print(maquina_de_escrever.escrever())
# print(escritor.ferramenta.escrever())

#________________________________________________

#Agregação - Os métodos de uma classe necessitam dos métodos da outra classe para funcionarem perfeitamente, mesmo ambos podendo existsir separadamente sem erro ao código

# class CarrinhoDeCompras:
#     def __init__(self):
#         self._produtos = []

#     def total(self):
#         return sum([p.preco for p in self._produtos])
    
#     def inserir_produtos(self, *produtos):
#         for produto in produtos:
#             self._produtos.append(produto)
    
#     def listar_produtos(self):
#         print()
#         for produto in self._produtos:
#             print(produto.nome, produto.preco)
#         print()

# class Produto:
#     def __init__(self, nome, preco):
#         self.nome=nome
#         self.preco=preco


# carrinho = CarrinhoDeCompras()
# p1, p2 = Produto('Caneta', 1.20), Produto('Carne', 19)     
# carrinho.inserir_produtos(p1, p2)           #A classe CarrinhoDeCompras possui produtos da classe Produtos
# carrinho.listar_produtos()
# print(carrinho.total())

#_______________________________________

#Composição - Na composição os objetos são inteligados onde apagando o objeto principal todos os outros são apagados

#_____________________

# class Carro:
#     def __init__(self, nome):
#         self.nome=nome
#         self._motor=None
#         self._fabricante=None
        

#         @motor.setter
#         def motor(self, valor):
#             self._motor=valor

#         @property
#         def motor(self):
#           return self._motor
        

#         @fabricante.setter
#         def fabricante(self, nome):
#           self.fabricante=nome


#         @property
#         def fabricante(self):
#           return self._fabricante



# class Motor:
#     def __init__(self, nome):
#         self.nome=nome



# class Fabricante:
#     def __init__(self, nome):
#         self.nome=nome

#_______________________

#Herança -  As classes herdam os parematros da classe principal

# class Pessoa:
#     def __init__(self, nome, sobrenome):
#         self.nome=nome
#         self.sobrenome=sobrenome


#     def falar_nome_classe(self):
#         print(self.nome, self.sobrenome, '-', self.__class__.__name__)


# class Cliente(Pessoa):
#     ...

# class Aluno (Pessoa):
#     ...


# c1=Cliente('Luiz', 'Otávio')
# c1.falar_nome_classe()
# a1=Aluno('André', 'Lima')
# a1.falar_nome_classe()

#________________________
# from pathlib import Path
# import os

# # Definindo o LOG_FILE corretamente
# LOG_FILE = Path(os.path.abspath(__file__)).parent / 'log.txt'

# class Log:
#     def _log(self, msg):
#         raise NotImplementedError('Implemente o método log')
#     def log_error(self, msg):
#         return self._log(f'Error: {msg}')
#     def log_success(self, msg):
#         return self._log(f'Success: {msg}')

# class LogFileMixin(Log):
#     def _log(self, msg):
#         msg_formatada = f'{msg} ({self.__class__.__name__})'
#         print('Salvando no log:', msg_formatada)
#         with open(LOG_FILE, 'a') as arquivo:
#             arquivo.write(msg_formatada)
#             arquivo.write('\n')

# class LogPrintMixin(Log):
#     def _log(self, msg):
#         print(f'{msg} ({self.__class__.__name__})')

# # Exemplo de uso
# # if __name__ == "__main__":
# #     log = LogFileMixin()
# #     log.log_success("Teste de sucesso")
# #     log.log_error("Teste de erro")



# class Eletronico:
#     def __init__(self, nome) :
#         self._nome = nome
#         self._ligado = False

#     def ligar(self):
#         if not self._ligado:
#             self._ligado = True

#     def desligar(self):
#         if self._ligado:
#             self._ligado=False

# class Smartphone(Eletronico, LogPrintMixin):
#     def ligar(self):
#         super().ligar()

#         if self._ligado:
#             msg=(f'{self._nome} está ligado')
#             self.log_success(msg)

#     def desligar(self):
#         super().desligar()

#         if not self._ligado:
#             msg=(f'{self._nome} está desligado')
#             self.log_error(msg)

#___________________________

# class Ponto:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __repr__(self):  #método mágico para retornar o nome da classe de forma legível
#         class_name = type(self).__name__
#         return f'{class_name}(x = {self.x!r}, y = {self.y!r})'
    

#     def __add__(self, other):  # Método mágico para retornar o resultado sempre que houver soma
#         novo_x = self.x + other.x
#         novo_y = self.y + other.y
#         return Ponto(novo_x, novo_y)
    

#     def __sub__(self, other):  #método mágico para retornar resultado sempre que houver subtração
#         novo_x = self.x - other.x
#         novo_y = self.y - other.y
#         return Ponto(novo_x, novo_y)

#     def __gt__(self, other): #método para verificar o maior
#         resultado_self = self.x + self.y
#         resultado_other = other.x + other.y
#         return resultado_self > resultado_other



# class Ponto:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

    
#     def __repr__(self):
#         class_name = type(self).__name__
#         return f'{class_name}(x={self.x}, y={self.y})'
    

#     def __add__(self, other):
#         novo_x = self.x + other.x
#         novo_y = self.y + other.y
#         return Ponto(novo_x, novo_y)
    
#     def __sub__(self, other):
#         novo_x = self.x - other.x
#         novo_y = self.y - other.y
#         return Ponto(novo_x, novo_y)
    
#     def __gt__(self, other):
#         resultado_self = self.x + self.y
#         resultado_other = other.x + other.y
#         return resultado_self > resultado_other


# if __name__ == '__main__':
#     P1 = Ponto(8, 9)
#     P2 = Ponto(2, 5)
#     print(P1, P2)
#     P3 = P1 + P2
#     print(P3)
#     P4 = P1 - P2
#     print(P4)
#     print('P1 é maior que P2', P1>P2)
#     print('P1 é menor que P2', P1<P2)

#__________________________________________________________

# def adicionar_repr(cls):
#     def my_repr(self):
#         class_name= type(self).__name__
#         class_dict = self.__dict__
#         class_repr = f'{class_name}{class_dict}'
#         return class_repr
#     cls.__repr__ = my_repr
#     return cls

# #adicionar_repr é usado com decorador para decorar as classes sem precisar ficar repetindo o codigo dentro de todas

# @adicionar_repr
# class Time:
#     def __init__(self, nome):
#         self.nome=nome

# @adicionar_repr
# class Planeta:
#     def __init__(self, nome):
#         self.nome=nome


#______________

# from typing import Any


# class CallMe:
#     def __init__(self, phone):
#         self.phone = phone

    
#     def __call__(self, nome):  #método especial __call__ permite executar a instancia além da classe
#         print(nome, 'está ligando para', self.phone)


# call1 = CallMe('83 987265699')
# call1('Cleyson')

#__________

# def cabecalho(msg):
#     print('='*42)
#     msg('BANCO24H')
#     print(msg.center(42, "="))
#     print('='*42)
    

# import abc

# class Conta(abc.ABC):
#     def __init__(self, agencia, conta, saldo=0):
#         self.agencia = agencia
#         self.conta = conta
#         self.saldo = saldo


#     @abc.abstractmethod
#     def sacar(self, valor): ...


#     def depositar(self, valor):
#         self.saldo += valor
#         self.detalhes (f'\033[0;32m(DEPÓSITO DE{valor:.2f}R$)\033[m')    


#     def detalhes(self, msg=''):
#         print(f'Seu Saldo é: {self.saldo:.2f}R${msg}')
#         print('--')


# class ContaPoupanca(Conta):
#     def sacar(self, valor):
#         valor_pos_saque =  self.saldo - valor
    
#         if valor_pos_saque >= 0:
#             print('\033[0;32mSAQUE APROVADO!\033[m')
#             self.saldo -= valor
#             self.detalhes(f' (VALOR SACADO: \033[0;31m{valor:.2F}R$)\033[m')
#             return self.saldo
        

#         print('\033[0;31mNÃO FOI POSSÍVEL SACAR O VALOR DESEJADO\033[m')
#         self.detalhes(f'(SAQUE NEGADO: {valor:.2f}R$)')

#     def __repr__(self) -> str:
#         class_name = type(self).__name__
#         attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r})'
#         return f'{class_name}{attrs}'


# class ContaCorrente(Conta):
#     def __init__(self, agencia, conta, saldo=0, limite=0):
#         super().__init__(agencia, conta, saldo)
#         self.limite = limite

#     def sacar(self, valor):
#         valor_pos_saque =  self.saldo - valor
#         limite_maximo = -self.limite
    
#         if valor_pos_saque >= limite_maximo:
#             print('\033[0;32mSAQUE APROVADO!\033[m')
#             self.saldo -= valor
#             self.detalhes(f' (VALOR SACADO: \033[0;31m{valor:.2F}R$)\033[m')
#             return self.saldo
        

#         print('\033[0;31mNÃO FOI POSSÍVEL SACAR O VALOR DESEJADO\033[m')
#         print(f'SEU LIMITE É DE \033[0;33m{self.limite:.2f}\033[m')
#         self.detalhes(f'(SAQUE NEGADO: {valor:.2f}R$)')

#     def __repr__(self) -> str:
#         class_name = type(self).__name__
#         attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r}, {self.limite!r})'
#         return f'{class_name}{attrs}'


# class Pessoa:
#     def __init__(self, nome: str, idade: int) -> None:
#         self.nome=nome
#         self.idade=idade

#     @property
#     def nome(self):
#         return self._nome
    
#     @nome.setter
#     def nome(self, nome: str):
#         self._nome= nome

#     @property
#     def idade(self):
#         return self._idade
    
#     @idade.setter
#     def idade(self, idade: int):
#         self._idade = idade


#     def __repr__(self) -> str:
#         class_name = type(self).__name__
#         attrs = f'({self.nome!r}, {self.idade!r})'
#         return f'{class_name}{attrs}'

# class Cliente(Pessoa):    
#     def __init__(self, nome: str, idade: int) -> None:
#         from typing import Union
#         super().__init__(nome, idade)
#         self.conta: Conta | None = None


# class Banco:
#     def __init__(
#         self,
#         agencias: list[int] | None = None,
#         clientes: list[Pessoa] | None = None,
#         contas: list[Conta] | None = None,
#     ):
#         self.agencias = agencias or []
#         self.clientes = clientes or []
#         self.contas = contas or []

#     def _checa_agencia(self, conta):
#         if conta.agencia in self.agencias:
#             print('_checa_agencia', True)
#             return True
#         print('_checa_agencia', False)
#         return False

#     def _checa_cliente(self, cliente):
#         if cliente in self.clientes:
#             print('_checa_cliente', True)
#             return True
#         print('_checa_cliente', False)
#         return False

#     def _checa_conta(self, conta):
#         if conta in self.contas:
#             print('_checa_conta', True)
#             return True
#         print('_checa_conta', False)
#         return False

#     def _checa_se_conta_e_do_cliente(self, cliente, conta):
#         if conta is cliente.conta:
#             print('_checa_se_conta_e_do_cliente', True)
#             return True
#         print('_checa_se_conta_e_do_cliente', False)
#         return False

#     def autenticar(self, cliente: Pessoa, conta: Conta):
#         return self._checa_agencia(conta) and \
#             self._checa_cliente(cliente) and \
#             self._checa_conta(conta) and \
#             self._checa_se_conta_e_do_cliente(cliente, conta)

#     def __repr__(self):
#         class_name = type(self).__name__
#         attrs = f'({self.agencias!r}, {self.clientes!r}, {self.contas!r})'
#         return f'{class_name}{attrs}'


#_______________________________

#dataclass
#Com dataclass não precisa declarar __init__, __repr__, __eq__(entre outros)

# from dataclasses import asdict, astuple, dataclass

# @dataclass
# class Pessoa:
#     nome: str
#     idade: int

# p1 = Pessoa('Cleyson', 22)
# print(p1)
# p2 = Pessoa('Cleyson', 22)
# print(p2 == p1)

# print(asdict(p1)) #transforma a dataclass em dicionário
# print(astuple(p2)) #transforma a dataclass em tuplas

import abc
from dataclasses import dataclass
from operator import contains

class Conta(abc.ABC):
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    @abc.abstractmethod
    def sacar(self, valor):...

    def depositar(self, valor):
        self.saldo += valor
        self.detalhes (f' (Depósito de {valor:.2f}R$)')
      
    
    def ver_saldo(self):
        print(self.saldo)

    def detalhes(self, msg=''):
        print(f'Seu saldo é de {self.saldo:.2f}R${msg}')
        print('--'*25)
        

class ContaPoupanca(Conta):
    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor

        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhes (f' (Saque no valor de {valor:.2f}R$ autorizado!)')
            
        print('Não foi possível sacar o valor desejado!')
        self.detalhes()
        
    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = (f'{self.agencia!r}, {self.conta!r}')
        return f'{class_name}: {attrs}'
    


class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo=0, limite=0):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor):
        saldo_pos_saque = self.saldo - valor
        limite_maximo = -self.limite

        if saldo_pos_saque >= limite_maximo:
            self.saldo -= valor
            print(f'Saque no valor de {valor:.2f}R$ aprovado')
            self.detalhes()


        elif valor > self.saldo:
            self.limite += self.saldo
            self.saldo = 0
            print(f'Saque no valor de {valor:.2f}R$ aprovado')
            self.detalhes()
            self.limite -= valor
            print(' Retirado valor do limite para completar valor de saque')
            print(self.limite)

        else:
            print(f'Saque no valor de {valor:.2f}R$ negado!')
            print(f'Seu limite é de {self.limite:.2f}R$')
            self.detalhes()

    def __repr__(self):
        class_name = type(self).__name__
        sttr = f'{self.agencia!r}, {self.conta!r}, {self.limite!r}'
        return f'{class_name}: {sttr}'





cp1 = ContaCorrente(222, 123, 6, 100)
cp1.depositar(5)
print(cp1)
cp1.sacar(7)
cp1.sacar(105)