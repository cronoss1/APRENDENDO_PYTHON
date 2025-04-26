# Exercícios de nível 4:

# EX_16:

soma = 0

while True:
    if soma < 50:
        soma += 5
        print(soma)
    else:
        break

# EX_17:

numero = 11

while True:
    if numero > 0:
        numero -= 1
        print(numero)
    else:
        break
# EX_18:

numero_1 = float(input('Digite um número: '))
numero_2 = float(input('Digite um número: '))
numero_3 = float(input('Digite um número: '))

multiplicacao = numero_1 * numero_2 * numero_3

print(f"A multiplicação dos números é: {multiplicacao}")

# EX_19:

nome = input("Digite seu nome: ")
sobre_nome = input("Digite seu sobrenome: ")
nome_completo = nome + " " + sobre_nome

print(f"Seu nome completo é: {nome_completo}")

# EX_20:

numero = 10
numero *= 3
print(numero)

