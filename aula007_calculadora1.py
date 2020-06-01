# def soma(a, b):
#     return a + b
#
# print(soma(1, 2))
# print(soma(3, 4))
#
# def subtracao(a, b):
#     return a - b
#
# print(subtracao(10, 2))
# print(subtracao(7, 8))
#
# def multiplicacao(a, b):
#     return a * b
#
# print(multiplicacao(3, 5))
# print(multiplicacao(3, 4))
#
# def divisao(a, b):
#     return a / b
#
# print(divisao(3, 4))
# print(divisao(3, 5))

class Calculadora:
    def __init__(self, num1, num2):
        self.a = num1
        self.b = num2

    def soma(self):
        return self.a + self.b

    def subtracao(self):
        return self.a - self.b

    def multiplicacao(self):
        return self.a * self.b

    def divisao(self):
        return self.a / self.b

if __name__ == '__main__':
    calculadora = Calculadora(10, 2)
    print(calculadora.soma())
    print(calculadora.subtracao())
    print(calculadora.multiplicacao())
    print(calculadora.divisao())
