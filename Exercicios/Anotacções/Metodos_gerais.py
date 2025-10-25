#Lista de metodos uteis para uso geral.

# Conversão de tipos
numero = int("123")      # Converte texto para número
texto = str(456)         # Converte número para texto
lista = list("abc")      # ['a', 'b', 'c']

# Entrada do usuário (sempre retorna texto)
nome = input("Qual seu nome? ")

# Comprimento
print(len("python"))     # 6 (texto)
print(len([1, 2, 3]))    # 3 (lista)
print(len({"a": 1}))     # 1 (dicionário)

# Range (para loops)
print(list(range(5)))    # [0, 1, 2, 3, 4]
print(list(range(1, 6))) # [1, 2, 3, 4, 5]