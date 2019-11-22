#!/usr/bin/python3
#PRIMEIRO EXERCICIO
#IMPRIME O NOME DO TIME

#print(input('qual o nome do time : '))

#SEGUNDO EXERCICIO
#FACA UM NUMERO QUE PECA UM NUMERO E IMPRIMA ESSE NIMERO

#varNumber = int(input('Digite um numero : '))

#print(varNumber)

#TERCEIRO EXERCICIO

# primeironumero = 5
# segundonumero = 23
# terceironumero = 25

# print(primeironumero+segundonumero+terceironumero)

#QUARTO EXERCICIO

# linguagem = 'python'
# if linguagem == 'python':
#     print('A linguagem é Pyton')
# else:
#     print('A linguagem não é Pyton')

#QUINTO EXERCICIO
#FACA UM PROGRAMA QUE RECEBA 'F' OU 'M' E MOSTRE FEMININO OU MASCULINO

# varSexo = str(input('Informe F ou M : '))
# varSexo = varSexo.capitalize()

# if varSexo == 'F':
#     print('O sexo é feminimo')
# elif varSexo == 'M':
#     print('Masculino')
# else:
#     print('Valor inválido')

#SEXTO EXERCICIO
#FACA UM PROGRAMA QUE PEÇA UM VALOR E MOSTRE NA TELA SE O VALOR É POSITIVO OU NEGATIVO



# try:
#     varNumero = float(input('Forneça um numero : '))
#     if varNumero > 0:
#         print(str(varNumero) + ' é um Numero é positivo')
#     elif varNumero == 0:
#         print(str(varNumero) + ' é Zero')
#     else:
#         print(str(varNumero) + ' é um numero é negativo')
# except ValueError as e:
#     print('Deu erro ...')

#TESTAR NO EXCEPT O EXCEPTION    

#SETIMO EXERCICIO
#listas 

# lista = [1,2,'abacaxi','laranja','moto',52,1,2,2,2,3,3,4,5,6,5,5,1]
# lista2 = [[1,2,3],['carro','moto','bike'],['casa','apartamento']]


# # lista.append('Carro')
# # lista.pop(3)
# # lista.insert(3,'laranja')
# # lista.reverse()
# # lista.reverse()
# #lista.pop(1) #remove com o pop usando o nome do ite3m da lista
# #lista.sort
# #print(lista.count('moto'))

# lista2[0][1]=50
# print(lista2)

# #oitavo exercicio
# lista = ['Corinthians', [1, 2, 3, 4, 5] ,'Palmeiras', 'São Paulo', [10, 11, 12, 13, 14],'Flamengo', 'Vasco']

# # dada a lista ['Corinthians', [1, 2, 3, 4, 5] ,'Palmeiras', 'São Paulo', [10, 11, 12, 13, 14],'Flamengo', 'Vasco']
# # print 3, 13, vasco
# print(lista[1][2], lista[4][3], lista[6])
# # print 5, São Paulo, 14
# print(lista[1][-1], lista[3], lista[4][4])
# # mudem o valor do 4 = 30
# lista[1][3] = 30
# # mudem o valor do 10 = 100
# lista[4][0] = 100
# # mudem o valor do 14 = 150
# lista[4][-1] = 150
# # mudem o valor vasco = Bragantino   
# lista[-1] = 'Bragantino'

# # print(lista)

# #tupla = (1,2,4,5,6,1,1)
# tupla = ('Python','java','PHP')

# #print(tupla[1].title())

# tupla[0].upper.

#dicionarios
#Decima primeira

# dicionario = {'nome':'Ronaldo','Sobrenome':'Ramires','Idade':46}
# dicionario['Nome']='João'
# print(dicionario)
# print(dicionario['nome'])
# print(dicionario['Sobrenome'])
# print(dicionario['Idade'])
# print(dicionario.keys())
# print(dicionario.values())


# conversao de tipos

# variavel = 15

var = 15

# peça que o usuaruio digite um numero e multiplique por var

# print(int(input('Digite um numero qualquer : ')) * var)

# faca uma lista com 10 nomes de usuarios
# peca para o usuario digitar o nome de usuario
# caso nao exista esse usuario na lista
# de um nameError volte para a parte 2

# lista_usuarios = ['Joao','Maria','Joaquim','Pedro','Luana','Zeca','Juca','Luiz','Roberto','Manoeli']

# while True:
#     try:
#         nome_usuario = input('digite o nome de usuario : ')
#         if nome_usuario.lower() not in lista_usuarios:
#             raise NameError('Esse usuarioo nao existe !!! ')
#         else:
#             print(f'Bem vindo(a) {nome_usuario}')
#             break
#     except NameError as e:
#         print(e)


# 19-11-19
# crie uma função que peça 2 numeros e retorne o maior
# se o valor for igual retorna valores iguais
# guarde em variavel e print



# def nMaior(n1, n2):
#     if n1 == n2:
#         return 'valores iguais'
#     elif n1 > n2:
#         return n1
#     else:
#         return n2

# var = nMaior(10,20)
# print(var)

# var = nMaior(10,10)
# print(var)

# var = nMaior(25,20)
# print(var)

# crie uma funcao que recba um numero indefinido de valroes numerocos 
# com *arg e retorne os alores ordenados de forma decrescente

# def ordenarValores(*var):
#     return sorted(var, reverse=True)

# var1 = ordenarValores(1,2,9,4,8,9)
# print(var1)    


# aula polimorfismo e heranca

# crie uma cklasse que represente um automovel

# com os atributos

# ano de fabricacao
# marca
# preco

# e os metodos

# get_ano
# get_marca
# get_preco

class Automovel():
    '''Clase que representa os automoveis'''
    def __init__(self,ano,marca,preco):
        self.ano = ano
        self.marca = marca
        self.preco = preco

    def get_ano(self):
        print(self.ano)

    def get_marca(self):
        print(self.marca)

    def get_preco(self):
        print(self.preco)

# carro = Automovel(1999,'Honda',25000)

# carro.get_ano()
# carro.get_marca()
# carro.get_marca()

# crie uma classe Moto e terá os atributos
# o atributo tipo
# e herdara os atributos/metoso da classe automovel

ligada = False

class Moto(Automovel):
    '''Classe que representa uma moto'''

    def __init__(self,ano,marca,preco,tipo):
        super().__init__(ano, marca, preco, tipo)
        self.tipo = tipo

    def ligar(self):
        global ligada
        try:

            if self.ligada == false:
                print('Ligando...')
                print('Ligada...')
                ligada = True
            else:
                raise TypeError('Moto Ligada'):
                print('Moto Ligada ...')
        except TypeError as motoligada:
            print('Moto ligda')

    def desligar(self):
        self.desligada = False
        try:

            if self.desligada == false:
                print('Desligando...')
                print('Desligada...')
                ligada = False
            else:
                raise TypeError('Moto desligada...')
        except TypeError as motodesligada:
            print(motodesligada)

    def acelerar(self):
        try:
            if self.ligada == False:
                raise TypeError('Moto desligada')
        except TypeError as motodesligada:
            print(motodesligada)

    def frear(self):
        global ligada
        try:
            if self.ligada == False:
                raise TypeError('Moto desligada')
        except TypeError as motodesligada:
            print(motodesligada)



# e os metodos

# ob: lembre-seque a moto so pode ligar se estiver desligada
# e desligar quando ligada
# acelerar e frear tambem só ligada
# ligar, desligar, acelerar, frear



