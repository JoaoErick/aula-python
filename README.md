# Introdução ao Python
Conteúdo introdutório à linguagem Python desenvolvido através do acompanhamento das aulas disponibilizadas pela Digital Innovation One juntamente com o professor Rafael Galleani (Líder Técnico na Global Hitss).  
https://digitalinnovation.one    

![](https://lh3.googleusercontent.com/proxy/9BsThedoq7SZSb2bzcWN7ZRJAVkcLDLuSyg2EQYy24jfjky_QXgaFSpv1QObY5-V9PbcSUHBIN7c9Y0CnRo4j8rWz03lVUyoLgnOjQIBvNDvlt7byXtnB0RH1nMiAuzd)
> Fonte: Developer News (2020)  
-------------

### Conteúdos Abordados 

* Variáveis, Strings e Inteiros.
* Print e Input.
* Operadores aritméticos e relacionais.
* Estruturas condicionais.
* Laços de repetição.  
* Listas, tuplas e suas operações.
* Conjuntos e Subconjuntos.
* Métodos, funções e classes.
* Módulos, importação de classes e funções anônimas (lambda).
* Trabalho com arquivos externos.
* Informações de data e hora.
* Gerenciamento e criação de exceções.
* Instalação e uso de pacotes (requisição com requests)
-------------

### Exemplo 1 - Python　

```python
a = int(input('Digite um número: '))
div = 0
for x in range(1, a+1):
    resto = a % x
    if resto == 0:
        div += 1

if div == 2:
    print('número {} é primo!'.format(a))
else:
    print('número {} não é primo!'.format(a))
```  
-------------

### Exemplo 2 - Python

```python
def contador_letras(lista_palavras):
    contador = []
    for x in lista_palavras:
        quantidade = len(x)
        contador.append(quantidade)
    return contador

if __name__ == '__main__':
    lista = ['cachorro', 'gato']
    print(contador_letras(lista))
```  
-------------

### Exemplo 3 - Python

```python
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
```  
-------------
### Fim

