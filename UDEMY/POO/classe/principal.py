from classe import *

#class Pessoa:
    # P1 = Pessoa('Cleyson', 'Lima', 23)
    # print(P1.nome)
    # P1.comer('carne')
    # P1.falar()
    # P1.Parar_de_Comer()
    # P1.falar()
    # P1.comer('carne')
    # P1.Parar_de_Falar()
    # P1.comer('carne')

#print(p1.__dict__) ou print(vars(p1)) exibe o dicionário com os valores de P1('Cleyson', 'Lima', 23)

# class Conection:
    # c1 = Conection()
    # c1.set_user('Luiz')
    # c1.set_pasword(1234)
    # print(c1.user)
    # print(c1.pasword)


# @classmethod
# c1 = Conection.create_with_auth('Luiz', 1234)
# print(c1.user, c1.pasword)

# caneta = Caneta('Azul')
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())

#________________

# Fusca = Carro('Fusca')
# volkswagen = Fabricante('volkswagen')
# Fusca.fabricante = volkswagen
# motor_1_0 = Motor('1.0')
# Fusca.motor = motor_1_0

# print(Fusca.nome, Fusca.fabricante.nome, Fusca.motor.nome)


# Uno = Carro('Uno')
# Fiat = Fabricante('Fiat')
# Uno.fabricante = Fiat
# Uno.motor = motor_1_0

# print(Uno.nome, Uno.fabricante.nome, Uno.motor.nome)

#_____________________________


# Redmi_note_12 = Smartphone('Redmi_note_12')
# Iphone_15 = Smartphone('Iphone_15')


# Redmi_note_12.ligar()
# Iphone_15.desligar()


#________________________

# if __name__ == '__main__':
#     P1 = Ponto(4, 2)
#     P2 = Ponto(6, 4)
#     P3 = P1 + P2
#     P4 = P1 - P2
#     print(P3)
#     print(P4)
#     print('P1 é maior que P2', P1>P2)
#     print('P2 é maior que P1', P2>P1)

#__________________________________

# Corinthians = Time('Corinthians')
# Fluminense =  Time('Fluminense')
# Terra = Planeta('Terra')
# Marte = Planeta('Marte')
# print(Corinthians)
# print(Fluminense)
# print(Terra)
# print(Marte)
#

#_____________________

# cp1 = ContaPoupanca(222, 111, 0)
# cp1.sacar(1)
# cp1.depositar(8)
# cp1.sacar(3)
# print('##')
# cc1 = ContaCorrente(222, 111, 0, 100)
# cc1.sacar(1)
# cc1.depositar(8)
# cc1.sacar(3)
# cc1.sacar(99)
# cc1.sacar(200)
# cc1.sacar(5)
# print('##')
# c1 = Cliente('Luiz', 30)
# cc1 = ContaCorrente(111, 222, 0, 0)
# c1.conta = cc1
# c2 = Cliente('Maria', 18)
# cp1 = ContaPoupanca(112, 223, 100)
# c2.conta = cp1
# banco = Banco()
# banco.clientes.extend([c1, c2])
# banco.contas.extend([cc1, cp1])
# banco.agencias.extend([111, 222])

# if banco.autenticar(c1, cc1):
#     cc1.depositar(10)
#     c1.conta.depositar(100)
#     print(c1.conta)
