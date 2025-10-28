# Exercícios de nível 1:

# EX_1:

numero = float(input("Digite um número: "))

if numero > 0:
    print("O número é positivo")
else:
    print("O número é negativo")

# EX_2:

idade = int(input("Digite sua idade: "))
if idade > 18:
    print("Você é maior de idade")
else:
    print("Você é menor de idade")

# EX_3:

numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print("O número é par")
else:
    print("O número é ímpar")

# EX_4:

senha = int(input("Digite sua senha: "))
senha_certa = 12345

if senha == senha_certa:
    print("Acesso permitido")
else:
    print("Acesso negado")

# EX_5:
numero = int(input("Digite um número: "))

if numero % 5 == 0:
    print("O número é múltiplo de 5")
else:
    print("O número não é múltiplo de 5")