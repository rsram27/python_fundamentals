# -*- coding : utf-8 -*-

'''
Software Old Bank
'''
class ContaBancaria():
    def __init__(self,cliente,conta,ag=8,banco=999,saldo=0):
        self.cliente = cliente
        self.conta = conta
        self.Agencia = ag
        self.banco = banco
        self.saldo = saldo
    
    def depositar(self):
        deposito = float(input('Digite o valor a ser depositado : R$'))
        print(f'Saldo anterior R${self.saldo}')
        print(f'Deposito : R${deposito}')
        self.saldo += deposito
        print(f'Novo saldo é R$ {self.saldo}')

    def sacar(self):
        saque = float(input('Informe o valore a ser sacado R$:'))
        if self.saldo < saque:
            print('Saldo insuficienet')

        else:
            print(f'Saldo anterior : R$ {self.saldo}')
            print(f'Saque R$ : {saque}')
            print(f'Novo saldo : R$ {self.saldo}')
    
    def extrato(self):
        print('Extrato')
        print('=' * 20)
        print(f'Agencia: 0: {self.Agencia} Conta: {self.conta}')
        print(f'Cliente : {self.cliente}')
        print(f'Saldo {self.saldo}')

cliente = ContaBancaria(input('Digite o nome do cliente : '),input('Digite o numero da conta: '))
print('Bem vindo(a) ao OldBank')
print('Selecione a opção abaixo')
print('Digite 1 para Extrato')
print('Digite 2 para Deposito')
print('Digite 3 para Saque')

opcao = int(input('> '))

try:
    if opcao == 1:
        cliente.extrato()
    elif opcao == 2:
        cliente.depositar()
    elif opcao == 3:
        cliente.sacar()
    else:
        print('Opção invalida')
except TypeError as e:
    print(e, 'Digite uma opção válida')
