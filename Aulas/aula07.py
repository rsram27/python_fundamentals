# # poo (herança e polimorfismo)

# class Pai():
#     '''Classe Pai'''

#     def __init__(self):
#         self.sobrenome = 'Pereira'

#     def get_sobrenome(self):
#         print(self.sobrenome)

# # class Filho(Pai):

# #     def __init__(self):
# #         super().__init__() # HERDA O ATRIBUTO

# class Animal():

#     def __init__(self, raca, idade):
#         self.raca = raca
#         self.idade = idade
#         self.olhos = True
#         self.orgaos = True

#     def Nascer(self):
#         print('Nasceu...')

#     def AlimentarSe(self):
#         print('Se alimentando...')

#     def Morrer(self):
#         print('Morreu...')
    
#     def get_raca(self):
#         print(self.raca)
    
#     def get_idade(self):
#         print(self.idade)


# class Mamifero(Animal):

#     def __init__(self, raca, idade):
#         super().__init__(raca, idade)

#         self.pele = True
#         self.mamilos = True

# cachorro = Mamifero('Pastor', 7)
# cachorro.get_raca()


# class Humano(Mamifero):

#     def __init__(self, nome, idade, pensa=True):
#         super().__init__()
#         self.nome = nome
#         self.idade = idade
#         self.pensa = pensa
#         self.bracos = 2
#         self.pernas = 2
#         self.cabeca = 1
#         self.tronco = 1
    
# humano1 = Humano('João', 21)

# print(humano1.nome, humano1.idade, humano1.pensa)

class Pai():
    
    def trabalhar(self):
        print('Trabalhando de engenheiro...')

class Filho():
    def trabalhar(self):
        print('Trabalhando de programador...')

joao = Pai()
joao.trabalhar()

joaquim = Filho()
joaquim.trabalhar()