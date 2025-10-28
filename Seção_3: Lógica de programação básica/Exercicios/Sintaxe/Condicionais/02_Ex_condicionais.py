# Exercícios de nível 2:

# EX_6:

idade = int(input("Digite sua idade: "))

if idade > 0 and idade <= 12:
    print("Você é uma criança.")
elif idade >= 13 and idade <= 17:
    print("Você é um adolescente.")
else:
    print("Você é um adulto.")

# EX_7:

lado_1 = float(input("Digite o comprimento do primeiro lado do triângulo: "))
lado_2 = float(input("Digite o comprimento do segundo lado do triângulo: "))
lado_3 = float(input("Digite o comprimento do terceiro lado do triângulo: "))

if lado_1 + lado_2 > lado_3:
    print("Os lados formam um triângulo.")
else:
    print("Os lados não formam um triângulo.")

# EX_8:

login = input("Digite seu login: ")
login_permitido = "admin"
idade = int(input("Digite sua idade: "))

if login == login_permitido or idade >= 18:
    print("Acesso permitido.")
else:
    print("Acesso negado.")

# EX_9:

numero = int(input("Digite um número: "))

if numero % 2 == 0 and numero % 3 == 0:
    print("O número é divisível por 2 e 3.")
else:
    print("O número não é divisível por 2 e 3.")

# EX_10:
compra = float(input("Digite o valor da compra: "))
clinte = input("Digite o tipo de cliente (1 - Normal, 2 - VIP): ")
desconto = 0.10

if clinte == "2" and compra > 100:
    valor_final = compra - (compra * desconto)
    print(f"Você tem direito ao desconto de 10%.\n"
    f"Valor final: {valor_final}.\n")
elif clinte == "1":
    print(f"Você não tem direito ao desconto de 10%.\n"
          f"Valor final: {compra}.\n")