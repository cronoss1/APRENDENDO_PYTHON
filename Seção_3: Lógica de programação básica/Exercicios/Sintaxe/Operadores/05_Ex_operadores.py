# Exercícios de nível 5:

# EX_21:

lista_1 = [1, 2, 3]
lista_2 = [1, 2, 3]
lista_3 = lista_1

if lista_1 == lista_2:
    print("Lista 1 tem o mesmo valor de Lista 3")
elif lista_1 is lista_3:
    print("Lista 3 é identica a lista 1")
else:
    print("Nenhuma das listas são iguais ou identicas")

# EX_22:

lista = ["mangas", "maçãs", "laranjas"]
item = input("Digite o item que deseja verificar se existe na lista: ")

if item in lista:
    print(f"O item {item} está na lista.")
else:
    print(f"O item {item} não está na lista")

# EX_23:

palavra = input("Digite uma palavra: ")

if "r" not in palavra:
    print("A letra 'r' não está na palavra")
else:
    print("A letra 'r' está na palavra")

# EX_24:

variavel_1 = 10
variavel_2 = variavel_1

if variavel_1 is variavel_2:
    print("A variável 1 é idêntica a variável 2")
else:
    print("A variável 1 não é idêntica a variável 2")

# EX_25:

dados = {
    "nome": "Lucas",
    "idade": 25,
    "cidade": "São Paulo"
}

if "nome" in dados:
    print("A chave (nome) está em dados")
else:
    print("A chave (nome) não está em dados")

