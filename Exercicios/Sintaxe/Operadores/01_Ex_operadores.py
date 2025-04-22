# Exercícios de nível 1:

# EX_1:

numero_1 = int(input("Digite um numero: "))
numero_2 = int(input("Digite mais um numero: "))
soma = numero_1 + numero_2
print(f"Resultado da soma: {soma}")

# EX_2:

numero_1 = int(input("Digite um numero: "))
numero_2 = int(input("Digite mais um numero: "))
subtracao = numero_1 - numero_2
if subtracao < 0:
    print(f"O Resultado da subtração é positivo: {subtracao}")
else:
    print(f"O Resultado da subtração é negativo: {subtracao}")

# EX_3:

numero = int(input("Digite um numero: "))
par = numero % 2

if par == 0:
    print(f"O numero {numero} é par")
else:
    print(f"O numero {numero} é impar")

# EX_4:

senha = int(input("Digite a senha: "))
senha_correta = 1234

if senha == senha_correta:
    print("Acesso Liberado!")
else:
    print("Acesso Negado!")

# EX_5:
numero = int(input("Digite um numero: "))
multiplo = numero % 5

if multiplo == 0:
    print(f"O numero {numero} é multiplo de 5")
else:
    print(f"O numero {numero} não é multiplo de 5")
