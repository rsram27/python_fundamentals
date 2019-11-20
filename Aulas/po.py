#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# class Servidor:
#     memoria = None
#     disco = None
#     cpu = None

# dns = Servidor()

# dns.memoria = 2048
# dns.disco = 50
# dns.cpu = 2

# print(f'O servidor tem as seguintes \
#         configurações : \nCPU: {dns.cpu},\nMemoria {dns.memoria}, \nDisco {dns.disco} ')


# class PrimeiraClasse:
#     def __init__(self):                      # self referencia o objeto que vai ser montado
#         print('Accessando o metodo construtor')

#     def metodo(self):
#         print('Acessando o metodo')


# classe = PrimeiraClasse()

# classe.metodo()


# # DICA DE AULA pip freeze >> requirements.txt
# # Cat requirements.txt

class Passaro():
    def __init__(self):
        self.asas = 2
        self.bico = 1
        self.penas = True
        self.patas = 2
        self.rabo = True
    
    def voar(self):
        self.t = 0
        if self.asas < 2:
            self.t = 1
            print('Passaro deficiente...')
        else:
            print('Voando...')
            self.t = 0

    def pousar(self):
        if self.t == 1:
            pass
        else:
            print('Pousando...')

    def dormir(self):
        print('Dormindo...')

    def acordar(self):
        print('Acordando...')

sabia = Passaro()
sabia.patas = 1
sabia.asas = 3
sabia.rabo = None
sabia.voar()
sabia.pousar()
sabia.dormir()
sabia.acordar()

