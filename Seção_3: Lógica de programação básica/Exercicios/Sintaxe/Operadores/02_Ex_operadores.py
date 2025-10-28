# Exercícios de nível 2:

# EX_6:

numero_1 = int(input("Digite o primeiro número: "))
numero_2 = int(input("Digite o segundo número: "))
if numero_1 > numero_2:
    print(f"{numero_1} é maior que {numero_2}")
elif numero_1 < numero_2:
    print(f"{numero_2} é maior que {numero_1}")
else:
    print(f"{numero_1} é igual a {numero_2}")

# EX_7:

numero_1 = int(input("Digite um número: "))
numero_2 = int(input("Dgite mais um número: "))
if numero_1 == numero_2 and numero_1 is numero_2:
    print("Valores iguais e Identicos")
elif numero_1 == numero_2: 
    print("Valores iguais")
else:
    print("Diferentes")

# EX_8:

numero = int(input("Digite um número: "))
if numero > 10 and numero < 20:
    print(f"O {numero} está entre 10 e 20.")
else:
    print(f"O {numero} não está entre 10 e 20.")

# EX_9:

numero = int(input("Digite um número: "))
verificacao = numero % 2

if verificacao == 0:
    print(f"O numero {numero} é par.")
else:
    print(f"O numero {numero} é impar.")

# EX_10:
numero_1 = int(input("Digite um número: "))
numero_2 = int(input("Digite mais um número: "))
divisivel = numero_1 % numero_2

if divisivel == 0:
    print(f"O {numero_1} é divisivel por {numero_2}.")
else:
    print(f"O {numero_1} não pe divisivel por {numero_2}.")