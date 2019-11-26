# -*- encoding = utf-8 -*-

# a = 2
# b = 2

# assert a == b, 'a é diferente b'
# assert a != b, 'a é igual a b'

# def soma(x, y):
#     return x + y

# def subtrair(x, y):
#     return x - y

# def dividir(x, y):
#     return x / y

# assert soma(2,2) == 4, f'Obtido {soma(2,2)}, Esperado: 4'
# assert soma(3,3) == 6, f'Obtido {soma(3,3)}, Esperado: 6'

# assert subtrair(2,2) == 0, f'Obtido {subtrair(2,2)}, Esperado: 0'
# assert subtrair(5,3) == 2, f'Obtido {subtrair(5,3)}, Esperado: 2'

# assert dividir(2,2) == 1, f'Obtido {dividir(2,2)}, Esperado: 1'
# assert dividir(12,3) == 4, f'Obtido {dividir(12,3)}, Esperado: 4'

# def somar(x, y):
#     return x + y

# def subtrair(x, y):
#     return x - y


def validar_par(num: int) -> bool:
    '''
    funcao para validad numero para
    arg
        num - recebe um numero do tipo inteiro
    Retorno booleano
    '''

    if isinstance(num, int):
        return True if num % 2 == 0 else False
    elif isinstance(num, str):
        if num.isnumeric():
            return True if int(num) % 2 == 0 else False
    else:
        return None