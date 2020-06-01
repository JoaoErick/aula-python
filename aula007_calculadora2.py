class Calculadora:
    def __init__(self):
        pass

    def soma(self, a , b):
        return a + b

    def subtracao(self, a, b):
        return a - b

    def multiplicacao(self, a, b):
        return a * b

    def divisao(self, a, b):
        return a / b

calculadora = Calculadora()
print(calculadora.soma(2, 5))
print(calculadora.subtracao(2, 5))
print(calculadora.multiplicacao(2, 5))
print(calculadora.divisao(2, 5))