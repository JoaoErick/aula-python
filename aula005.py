lista = [12, 10, 7, 5]
lista_animal = ['cachorro', 'gato', 'elefante', 'lobo', 'arara']
#print(lista_animal[1])

# for x in lista_animal:
#     print(x)
#
# soma = 0
# for x in lista:
#     print(x)
#     soma += x
# print(soma)

# print(sum(lista)) #Soma todos os valores da lista.
# print(max(lista)) #Maior valor da lista.
# print(min(lista)) #Menor valor da lista.

# if 'lobo' in lista_animal:
#     print('Existe um lobo na lista')
# else:
#     print('Não existe lobo na lista')
#     lista_animal.append('lobo') #Adiciona o lobo
#     print(lista_animal)
#     lista_animal.pop() #Remove o último elemento
#     print(lista_animal)
#     lista_animal.pop(0)  # Remove o elemento dessa posição
#     print(lista_animal)
#     lista_animal.remove('elefante') #Remove o elemento pelo nome.
#     print(lista_animal)

#nova_lista = lista_animal * 3 #Multiplica cada conteudo 3 vezes.

# lista.sort() #Ordena em ordem crescente.
# lista_animal.sort() #Ordena seguindo o alfabeto
# print(lista)
# print(lista_animal)
# lista_animal.reverse() #Ordena começando pela letra Z.
# print(lista_animal)

tupla = (1, 10, 12, 14) #Não é possível alterar os elementos da tupla --> print[0] = 12
print(len(tupla)) #Exibe a quantidade de elementos.
tupla_animal = tuple(lista_animal) #Converte lista para tupla
lista_numerica = list(tupla) #Converte tupla em lista.