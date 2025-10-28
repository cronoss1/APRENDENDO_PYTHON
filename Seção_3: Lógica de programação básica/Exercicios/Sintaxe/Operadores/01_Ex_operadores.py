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

numero_1 = float(input("Digite o primeiro número: "))
numero_2 = float(input("Digite o segundo número: "))
numero_3 = float(input("Digite o terceiro número: "))
multiplicacao = numero_1 * numero_2 * numero_3

print(f"Resultado: {multiplicacao}")

# EX_4:

numero_1 = float(input("Digite o primeiro número: "))
numero_2 = float(input("Digite o segundo número: "))
divisao = numero_1 / numero_2
resto = numero_1 % numero_2

print(f"\n A divisão de {numero_1} e {numero_2} é {divisao}"
    f" o resto da divisão é {resto} \n")

# EX_5:

numero = float(input("Digite um número: "))
raiz = numero ** 2

print(f"A raiz quadrada de {numero} é {raiz}")
