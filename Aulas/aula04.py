#!/usr/bin/python3

#while

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

#7 
# A mensagem "aprovadop" se a media alcancançada for maior ou igual a sete:

# A mensagem "reprovada" se a media for menor do que sete

# A mensagem "aprovada com distincao" se a media for igual a dez

nome_aluno = input('Digite o nome do aluno : ')

nota1 = float(input('Digite a primeira nota : '))
nota2 = float(input('Digite a segunda nota : '))

media_semestre = (nota1 + nota2) / 2

print(f'A nota do aluno {nome_aluno} é {media_semestre}')

if media_semestre == 10.0:
    print(f'Aluno {nome_aluno} foi aprovado com distinção')
elif media_semestre >= 7.0:
    print(f'Aluno {nome_aluno} foi aprovado')
else:
    print(f'Aluno {nome_aluno} foi reprovado')