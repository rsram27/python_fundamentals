#!/usr/bin/python3

# while

# x = 0
# y = 9
# while x < 10:
#     x += 1
#     print(x * y)

# x = 1

# while x <= 10:
#     print(f'numero :  {x}')
#     x += 1
# print('O while acabou')

# # a = 500

# # while a > 10:
# #     print(a)
# #     a -=10

# x = 1
# lista = []
# while x < 10:
#     lista.append(x)
#     x += 1

# print(lista)

# fruta = ['Laranja','Melancia','Uva']

# for f in fruta:
#     print (f)

# l = [1,2,3,4,5,6,7,8,9]

# for var in l:
#     print(var)

# frutas = ['abacaxi','banana','maça','abacate']

# for fruta in frutas:
#     print(fruta)

# # range ============>
# for item in range(99999,0,-1):
#     print(item)

# cont = 0

# while cont < 10:
#     print(f'vezes de execuacao {cont +1}')
#     if cont == 2:
#         print('bloco de condicao que interrompe o loop')
#         break
#     cont += 1

# t = 0

# while t < 10:
#     print(t)
#     if t == 5:
#         print('voltando')
#     t +=1
#     continue

# faca um programa a leitura de duas notas parciais
# de um aluno. O programa deve calucluar a media alcancada
# por aluno e apresentar

# 7
# A mensagem "aprovadop" se a media alcancançada for maior ou igual a sete:

# A mensagem "reprovada" se a media for menor do que sete

# A mensagem "aprovada com distincao" se a media for igual a dez

# nome_aluno = input('Digite o nome do aluno : ')

# nota1 = float(input('Digite a primeira nota : '))
# nota2 = float(input('Digite a segunda nota : '))

# media_semestre = (nota1 + nota2) / 2

# print(f'A nota do aluno {nome_aluno} é {media_semestre}')

# if media_semestre == 10.0:
#     print(f'Aluno {nome_aluno} foi aprovado com distinção')
# elif media_semestre >= 7.0:
#     print(f'Aluno {nome_aluno} foi aprovado')
# else:
#     print(f'Aluno {nome_aluno} foi reprovado')

# erros e exceçoes

# try:
#     if 'mariana' == nome:
#         print('nome correto')
#     else:
#         print('nome errado')
# except Exception as e:
#     print('Variavel nao atribuida',e)
# finally:
#     nome = 'Marina'
#     print(nome)

# try:
#     x = int(input('digite o prineiro numero : '))
#     y = int(input('digite o segundo numero : '))
#     print(x+y)
# except ValueError as v:
#     print(f'o erro é {v}')


# while True:
#     try:
#         idade = int(input('digite sua idade : '))
#         if idade < 16:
#             print('Voce nao pode comprar bebida alcoolica e nem \
#                 tirar titulo de eleitor')
#             break
#         else:
#             if idade >= 16 and idade < 18:
#                 print('pode ter titulo de eleitor')
#                 break
#             else:a
#                 print('voce pode comprar bebida e ter \
#                     titulo de eleitor')
#                 break
#             break

#     except Exception as e:
#         print('isso nao é um numero ', e)
#         continue

# while True:
#     try:
#         login = input('Digite o login : ')

#         if login.lower() == 'bryan':
#             raise NameError('Bryan esta banido')
#         else:
#             print(f'Bem vindo {login} ao sistema')
#             break
#     except NameError as e:
#         print(e)
#         continue

# revisao tratamento de erros

# while True:
#     try:
#         x = int(input('Digite o primeiro numenro : '))
#         y = int(input('Digite o segundo numero : '))
#         print(f'O valor calculado é : {x * y}')
#         break
#     except Exception as e:
#         print('Digite apenas numeros ', e)
#         continue

# usuarios : ['Ana','Caio','Joaquina']
# while True:
#     try:
#         user = input('Digite o nome de usuario: ')
#         if user == 'Ana':
#             raise NameError('Usuario Bloqueado!!')
#         else:
#             print(f' Bem Vindo ! ')
#             break
#     except NameError as n:
#         print(n)
#         continue

# manipulando arquivos

# arq1 = open('../Arquivos/sherlock.txt','r')

# # print(arq1.read()) le o arquivo
# # print(f'O arquivo tem : {arq1.tell()}') tell mostra a quantidade de caracteres do arquivo, usar o read antes
# # print(arq1.read(100)) Le até a posicao 100

# arq1.close()

# with open('arquivo01.txt','a') as f:
#     f.write(' Abrindo arquivos em python do Ramires \n')

arq1 = open('arquivo01.txt','r')
print(arq1.read())
arq1.close