# from aula09 import somar, subtrair
from aula09 import validar_par
from unittest import TestCase, main

# class Teste(TestCase):
#     def test_soma(self):
#         self.assertEqual(somar(2,2), 4)
#         self.assertLess(somar(2,3), 6)

#     def test_subtrair(self):
#         self.assertEqual(subtrair(5,5), 0)
#         self.assertLessEqual(subtrair(10,5),6)

# if __name__ == "__main__":
#     main()

def validar_par(num: int) -> bool:

    '''
    funcao para validar nume par
        num - recebe um numero do tipo inteiro
    retorno : booleano
    '''
    pass

class Teste(TestCase):
    def test_par(self):
        self.assertEqual(validar_par(4), True)
        self.assertEqual(validar_par(1000), True)
    def test_impar(self):
        self.assertEqual(validar_impar(5), False)
        self.assertEqual(validar_impar(1001), False)
    def test_string(self):
        self.assertEqual(validar_par('102'), True)
        self.assertEqual(validar_par('1059'),False)
        self.assertEqual(validar_par('string'), None)


if __name__ == "__main__":
    pass





