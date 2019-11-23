# -*- coding: utf-8 -*- 

# class Servidor:
#     memoria = None
#     disco = None
#     cpu = None


# dns = Servidor()

# dns.memoria = 2048
# dns.disco = 50
# dns.cpu = 2

# print(f'O servido tem as seguintes \
#        \nconfigurações: \nCPU: {dns.cpu},\
#        \nMemoria: {dns.memoria}, \
#        \nDisco: {dns.disco}')

# class PrimeiraClasse:

#     def __init__(self):
#         print('Acessando o método construtor')
    
#     def metodo(self):
#         print('Acessando método')


# print(PrimeiraClasse())

# class Passaro():

#     def __init__(self):
#         self.asa = 2
#         self.bico = 1
#         self.penas = True
#         self.patas = 2
#         self.rabo = True
    
#     def voar(self):
#         if self.asa < 2:
#             self.t = 1
#             print('Passaro deficiente')
#         else:
#             print('Voando...')
#             self.t = 0
    
#     def pousar(self):
#         if self.t == 1:
#             pass
#         else:
#             print('Pousando...')

#     def dormir(self):
#         print('Dormindo...')
    
#     def acordar(self):
#         print('Acordadndo...')


# sabia = Passaro()
# sabia.patas = 1
# sabia.asa = 1
# sabia.rabo = None

# sabia.voar()
# sabia.pousar()


import random

print(random.randrange(1, 100))





# crie uma classe que represente um automovel

# com os atributos:

# ano de fabricação;
# marca;
# preco;

# e os métodos:

# get_ano;
# get_marca;
# get_preco;


class Automovel():
    '''Classe que representa um automovel'''
    def __init__(self,ano, marca, preco):
        self.ano = ano
        self.marca = marca
        self.preco = preco
    
    def get_ano(self):
        print(self.ano)
    
    def get_marca(self):
        print(self.marca)

    def get_preco(self):
        print(self.preco)
        
# crie uma classe Moto que terá:
# o atributo tipo;
# e herdará os atributos/métodos da classe automovel

# e os métodos:


# obs. lembresse que a moto só pode ligar se estiver desligada 
# e desligar quando ligada
# acelerar e frear também só ligada
# ligar, desligar, acelerar, frear

ligada = False

class Moto(Automovel):
    '''Classe que representa uma Moto'''
    def __init__(self, ano, marca, preco, tipo='Moto'):
        super().__init__(ano, marca, preco)
        self.tipo = tipo

    def ligar(self):
        global ligada
        try:
            if ligada == False:
                print('Ligando...')
                print('Ligada...')
                ligada = True
            else:
                raise TypeError('Moto ligada')
        except TypeError as motoLigada:
            print(motoLigada)


    def desligar(self):
        global ligada
        try:
            if ligada == True:
                print('Desligando...')
                print('Desligada...')
                ligada = False
            else:
                raise TypeError('Moto desligada...')
        except TypeError as m:
            print(m)
    
    def acelerar(self):
        global ligada
        try:
            if ligada == True:
                print('Acelerando...')
            else:
                raise TypeError('Moto Desligada')
        except TypeError as motoDesligada:
            print(motoDesligada)
        
    def frear(self):
        global ligada
        try:
            if ligada == True:
                print('Freando...')
            else:
                raise TypeError('Moto Desligada')
        except TypeError as motoDesligada:
            print(motoDesligada)
        



cb125 = Moto(2010, 'Honda', 15.999)
cb125.ligar()
cb125.acelerar()
cb125.frear()
cb125.desligar()
cb125.get_ano()
cb125.get_marca()
cb125.get_preco()
