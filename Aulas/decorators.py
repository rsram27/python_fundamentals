# Decorator, exemplo basico

# def oi(nome='Pedro'):
#     return "oi " + nome

#     def ola():
#         return 'aqui voces esta na funcao ola()'

#     def boasvindas():
#         return 'aqui voces esta na funcao boasvindas()'


def inc(x):
    return x + 1

def dec(x):
    return x - 1


def operacao(func, x):
    resultado = func(x)
    return resultado

def soma_2(y):
    return y + 2

def printa(x):
    print(x)

(operacao(print,10))



