a = 10
b = 5
soma = a + b
multiplicacao = a * b
subtracao = a - b
divisao = a / b
resto = a % b

print(soma)
print(multiplicacao)
print(subtracao)
print(divisao)
print('{}\n'.format(resto))

print(type(soma)) #Imprime o tipo da variável.
soma = str(soma)  #Converte inteiro para string.
print('{}\n'.format(type(soma)))
soma = int(soma)

print('A soma é: ' + str(soma))
print('A soma é: {}'.format(soma)) #Maneira mais eficaz.
print('A soma é: {soma}\n'.format(soma=soma))

c = int(input('Digite um numero: '))
d = int(input('Digite outro numero: '))
print('A multiplição de {} X {} resulta em: {}'.format(c,d,c*d))