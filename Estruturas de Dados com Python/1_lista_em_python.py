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

numeros_1 = list(range(10)) # # Uma lista onde sera criando um elemento para cada numero da sequência

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
# Vai pegar da posição 0 até o ponto de parada o 2
print(lista[1:3])  # ["y", "t"]
# Vai pegar da posição 1 até o ponto de parada o 3
print(lista[0:3:2])  # ["p", "t"]
# Vai pegar da posição 0 até o ponto de parada o 3, andando de 2 em 2 posições
print(lista[::])  # ["p", "y", "t", "h", "o", "n"]
# Se tudo é vazio, tudo vai ser pego da lista
print(lista[::-1])  # ["n", "o", "h", "t", "y", "p"]

"""
Iterar Listas:
A forma mais comum para percorrer os dados de uma lista é utilizando o comando for.
"""
# Exemplo:
carros = ["gol", "celta", "palio"] # Lista

for carro in carros: # Usando for
    print(carro) # Monstrando as informações da lista na tela

"""
Compreensão de Listas:
A compreensão de lista oferece uma sintaxe mais curta quando você deseja: 
criar uma nova lista com base nos valores de uma lista existente (filtro) ou gerar uma nova lista 
aplicando alguma modificação nos elementos de uma lista existente.
"""
# Exemplo 1:
numeros_1 = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros_1:
    if numero % 2 == 0:
        pares.append(numero)

# Exemplo 2:
numeros_2 = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros_2 if numero % 2 == 0]

# Métodos da Classe list:
# [].append - Adiciona um novo elemento na lista

# [].clear - Utilizado quando eu quero limpar a minha lista

# [].copy - Ele vai retornar uma copia da lista que não afeta a original

# [].count - Usando para contar quantas vezes um objeto aparece na lista

# [].extend - Usado para adicionar mais de 1 elemento na lista 

# [].index - Usado para saber o index da primeira vez que ele aparece na lista

# [].pop - 

# [].remove - 

# [].reverse - 

# [].sort - 

# len - 

# sorted - 
