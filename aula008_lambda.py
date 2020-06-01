contador_letras = lambda lista: [len(x) for x in lista] #função anônima(sem nome) que retorna a qtd de letras por palavra

lista_animais = ['cachorro', 'gato', 'elefante']
print(contador_letras(lista_animais))

soma = lambda a, b: a + b
subtracao = lambda a, b: a - b
multiplicacao = lambda a, b: a * b
divisao = lambda a, b: a / b

print(soma(5,5))
print(subtracao(5,5))
print(multiplicacao(5,5))
print(divisao(5,5))

calculadora = { #Dicionário de calculadora
    'soma': lambda a, b: a + b,
    'subtracao': lambda a, b: a - b,
    'multiplicacao': lambda a, b: a * b,
    'divisao': lambda a, b: a / b
}

soma = calculadora['soma']
subtracao = calculadora['subtracao']
multiplicacao = calculadora['multiplicacao']
print('A soma é: {}'.format(soma(10,5)))
print('A multiplicacao é: {}'.format(multiplicacao(10,5)))
