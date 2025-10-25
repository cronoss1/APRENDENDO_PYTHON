#Lista de metodos uteis para usar com listas.
lista = [1, 2, 3]

# Adicionar elementos
lista.append(4)           # [1, 2, 3, 4]
lista.insert(1, 10)       # [1, 10, 2, 3, 4] (insere na posição 1)

# Remover elementos
lista.remove(10)          # [1, 2, 3, 4] (remove pelo valor)
ultimo = lista.pop()      # [1, 2, 3] (remove último)

# Informações
print(len(lista))         # 3 (quantidade)
print(2 in lista)         # True (verifica se está na lista)
print(lista.index(2))     # 1 (posição do elemento)

# Ordenação
numeros = [3, 1, 4, 2]
numeros.sort()            # [1, 2, 3, 4] (ordena)
numeros.reverse()         # [4, 3, 2, 1] (inverte)
