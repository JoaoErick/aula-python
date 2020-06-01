# conjunto = {1, 2, 3, 4}
# print(conjunto)
#
# conjunto = {1, 2, 3, 4, 4} #Não existem elementos duplicados
# print(conjunto)
#
# conjunto = {1, 2, 3, 4, 2}
# conjunto.add(5)
# print(conjunto)

# conjunto = {1, 2, 3, 4, 2}
# conjunto.discard(2)
# print(conjunto)

# conjunto = {1, 2, 3, 4, 5}
# conjunto2 = {5, 6, 7, 8}
# conjunto_uniao = conjunto.union(conjunto2)
# print('União: {}'.format(conjunto_uniao))
# conjunto_intersecao = conjunto.intersection(conjunto2)
# print('Interseção: {}'.format(conjunto_intersecao))
# conjunto_diferenca1 = conjunto.difference(conjunto2)
# conjunto_diferenca2 = conjunto2.difference(conjunto)
# print('Diferença entre 1 e 2: {}'.format(conjunto_diferenca1))
# print('Diferença entre 2 e 1: {}'.format(conjunto_diferenca2))
# conjunto_diff_simetrica = conjunto.symmetric_difference(conjunto2)
# print('Diferença simétrica: {}'.format(conjunto_diff_simetrica)) #O que tem de diferente nos dois conjuntos

conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}
conjunto_subset = conjunto_a.issubset(conjunto_b) #Verifia se um conjunto é subconjunto do outro.
print('A é subconjunto de B? {}'.format(conjunto_subset))
conjunto_superset = conjunto_b.issuperset(conjunto_a) #Verifica se um conjunto é superconjunto do outro.
print('B é superconjunto de A? {}'.format(conjunto_superset))

lista = ['cachorro', 'cachorro', 'gato', 'gato', 'elefante']
print(lista)
conjunto_animais = set(lista)
print(conjunto_animais)
lista = list(conjunto_animais)
print(lista)