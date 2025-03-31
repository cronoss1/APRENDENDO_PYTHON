# Listas em PYTHON
"""
Criando Listas:
Listas em Python podem armazenar de maneira sequencial qualquer tipo de objeto. 
Podemos criar listas utilizando o construtor list, a função range ou colocando 
valores separados por vírgula dentro de colchetes. Listas são objetos mutáveis, 
portanto podemos alterar seus valores após a criação
"""
# Exemplos:
frutas = ["laranja", "maca", "uva"] # Lista com valores, da forma mais comum

frutas = [] # Lista vazia

letras = list("python") # Uma lista onde cada letra é um elemento

numeros = list(range(10)) # # Uma lista onde sera criando um elemento para cada numero da sequência

carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True] 
# Uma lista onde tem varios elemento como str, int e boleano. 

"""
Acesso Direto:
A lista é uma sequência, portanto podemos acessar seus dados utilanzando índices.
Contamos o índice de determinada sequência a partir do zero.
"""
# Exemplo:
frutas = ["pera", "maçã", "laranja", "uva"] # Variavel frutas com a lista de frutas
#           0        1        2        3
#          -4       -3       -2       -1
print(frutas[0])  # Usando a sequência positiva para acessar os dados.
print(frutas[-1]) # Usando a sequência negativa para acessar os dados.

"""
Listas Aninhadas:
Listas podem armazenar todos os tipos de objetos Python, portanto podemos ter 
listas que armazenam outras listas. Com isso podemos criar estruturas bidimensionais (tabelas), 
e acessar informando os índices de linha e coluna. 
"""
# Exemplo:
matriz = [
    [1, "a", 2], # Linhas
    ["b", 3, 4],
    [6, 5, "c"]
] # Colunas

# Matriz bidimensionla com colunas e linhas
print(matriz[0]) # Acessando a linha 0 -> [1, a, 2]
print(matriz[0][0]) # Acessando a linha 0 e o elemento 0 -> 1
print(matriz[0][-1]) # Acessando a linha 0 e o elemento -1 -> 2
print(matriz[-1][-1]) # Acessando a linha -1 e o elemento -1 -> c

"""
Fatiamento:
Além de acessar elementos diretamente, podemos extrair um conjunto de valores de uma sequência. 
Para isso basta passar o índice inicial e/ou final para acessar o conjunto. 
Podemos ainda informar quantas posições o cursor deve "pular" no acesso.
"""
# Exemplo:
lista = ["p", "y", "t", "h", "o", "n"]
#         0    1    2    3    4    5
#        -6   -5   -4   -3   -2   -1

print(lista[2:])  # ["t", "h", "o", "n"]
# Vai pegar da posição 2 até a ultima
print(lista[:2])  # ["p", "y"]

print(lista[1:3])  # ["y", "t"]
print(lista[0:3:2])  # ["p", "t"]
print(lista[::])  # ["p", "y", "t", "h", "o", "n"]
print(lista[::-1])  # ["n", "o", "h", "t", "y", "p"]
