# CRIAÇÃO E ACESSO AOS DADOS
"""
Criando tuplas:
Tuplas são estruturas de dados muito parecidas com as listas, 
a principal diferença é que tuplas são imutáveis enquanto listas são mutáveis. 
Podemos criar tuplas através da classe tuple, ou colocando valores separados 
por vírgula de parenteses.
"""
# Exemplo:
frutas = ("laranja", "pera", "uva",)

letras = tuple("python")

numeros = tuple([1, 2, 3, 4])

pais = ("Brasil",)

"""
Acesso direto:
A tupla é uma sequência, portanto podemos acessar seus dados utilizando índices. 
Contamos o índice de determinada sequência a partir do zero.
"""
# Exemplo:


"""
Índices negativos:
Sequências suportam indexação negativa. A contagem começa em -1.
"""
# Exemplo:


"""
Tuplas aninhadas:
Tuplas podem armazenar todos os tipos de objetos Python, portanto podemos ter tuplas 
que armazenam outras tuplas. Com isso podemos criar estruturas bidimensionais (tabelas), 
e acessar informando os índices de linha e coluna. 
"""
# Exemplo:


"""
Fatiamento:
Além de acessar elementos diretamente, podemos extrair um conjunto de valores de uma sequência. 
Para isso basta passar o índice inicial e/ou final para acessar o conjunto. 
Podemos ainda informar quantas posições o cursor deve "pular" no acesso.
"""
# Exemplo:


"""
Iterar tuplas:
A forma mais comum para percorrer os dados de uma tupla é utilizando o comando for.
"""
# Exemplo:

"""
Função enumerate:
Às vezes é necessário saber qual o índice do objeto dentro do laço for. 
Para isso podemos usar a função enumerate.
"""
# Exemplo:
