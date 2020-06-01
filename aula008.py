from aula007_televisao import Televisao
from aula007_calculadora1 import Calculadora
from aula008_contador_letras import contador_letras

if __name__ == '__main__':
    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)

    calculadora = Calculadora(5, 10)
    print(calculadora.soma())

    lista = ['cachorro', 'gato', 'elefante']
    total_letras = contador_letras(lista)
    print('O total de letras por palavra da lista é: {}'.format(total_letras))


