lista = [1, 10]
arquivo = open('teste.txt', 'r')
try:
    #divisao = 10/0
    #numero = lista[3]
    #x = a
    x = 1
    #print('fechando arquivo')
    #arquivo.close()
except ZeroDivisionError: #Erro de divisões por zero
    print('Não é possível realizar divisão por zero')
except ArithmeticError:
    print('Houve um erro ao realizar uma operação aritmética')
except IndexError: #Erro de índice
    print('Erro ao acessar o índice inválido da lista')
except BaseException as ex: #BaseException é a Exceção pai de todas as outras; ex guarda a exceção gerada
    print(ex)
#except: #Erro genérico
    #print('Erro desconhecido')
else:
    print('Executa quando não houver nenhuma exceção')
finally:
    print('Sempre executa')
    print('fechando arquivo')
    arquivo.close()