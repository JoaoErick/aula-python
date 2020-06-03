import shutil

"""
arquivo = open('teste.txt', 'a') #(w = write) (r = read) (a = append)
#arquivo.write('Minha primeira escrita')
#arquivo.write('Segunda escrita') #Sobrescreve a linha
arquivo.write('\nSegunda escrita')
arquivo.write('\nTerceira escrita')

arquivo.close()
"""
def escrever_arquivo(texto):
    arquivo = open('teste.txt', 'w') #(w = write) (r = read) (a = append)
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)
    arquivo.close()

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    #print(aluno_nota)
    aluno_nota = aluno_nota.split('\n')
    #print(aluno_nota)
    lista_medias = []
    for x in aluno_nota:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        #print(lista_notas)
        print(aluno)
        media = lambda notas: sum([int(i) for i in notas]) / 4
        print(media(lista_notas))
        lista_medias.append({aluno: media(lista_notas)})
    arquivo.close()
    return lista_medias

def copia_arquivo(nome_arquivo):
    #shutil.copy(nome_arquivo, 'C:/Users/Suporte Ztha/PycharmProjects')
    shutil.copy(nome_arquivo, 'C:/Users/Suporte Ztha/PycharmProjects/notas_alunos.txt')

def move_arquivo(nome_arquivo):
    #shutil.move(nome_arquivo, 'C:/Users/Suporte Ztha/PycharmProjects/teste_novoNome')
    shutil.move(nome_arquivo, 'C:/Users/Suporte Ztha/PycharmProjects')


if __name__ == '__main__':
    escrever_arquivo('Primeira linha.\n')
    #aluno = '\nCesar, 7, 8, 5, 6'
    #atualizar_arquivo('notas.txt', aluno)
    #ler_arquivo('teste.txt')
    #media_notas('notas.txt')
    #lista_media = media_notas('notas.txt')
    #print(lista_media)
    #copia_arquivo('notas.txt')
    #move_arquivo('teste.txt')
