# Exercícios com (if) básico.
# 1.Positivo, negativo ou zero:
# Escreva um programa que peça ao usuário para digitar um número e determine se ele é positivo, negativo ou zero.

numero = int(input("Digite um numero: "))

if numero > 0:
    print(f"O numero {numero} é positivo.")
elif numero < 0:
    print(f"O numero {numero} é negativo.")
elif numero == 0:
    print("O numero é 0.")


# 2.Maior de idade:
# Peça ao usuário para informar sua idade. Se a idade for maior ou igual a 18, exiba "Você é maior de idade". Caso contrário, exiba "Você é menor de idade".

idade = int(input("Informe sua idade: "))

if idade >= 18:
    print("Você é maior de idade.")
elif idade < 18:
    print("Você é menor de idade.")


# 3.Par ou ímpar:
# Crie um programa que verifique se um número digitado pelo usuário é par ou ímpar. Dica: Use o operador % (resto da divisão).

numero = int(input("Digite um numero: "))

if numero % 2 == 0:
    print(f"O numero é par")
else:
    print("O numero é impar")


# Exercícios com (if-else) e (elif).
# 4.Classificação de notas:
# Peça ao usuário para digitar uma nota de 0 a 10. Classifique a nota da seguinte forma:

# 0 a 4: "Reprovado"

# 5 a 6: "Recuperação"

# 7 a 10: "Aprovado"

nota = float(input("Digite sua nota: "))

if nota <= 4:
    print("Você está de reprovado.")
elif nota <= 6:
    print("Você está de recuperação.")
elif nota <= 10:
    print("Você está aprovado.")


# 5.Comparação de números:
# Peça ao usuário para digitar dois números. Exiba uma mensagem informando qual número é maior ou se eles são iguais.

numero_1 = int(input("Digite um numero: "))
numero_2 = int(input("Digite mais um numero: "))

if numero_1 > numero_2:
    print(f"O numero {numero_1} é o maior")
elif numero_2 > numero_1:
    print(f"O numero {numero_2} é maior")
elif numero_1 == numero_2:
    print(f"Os numeros {numero_1} e {numero_2} tem o mesmo valor.")


# 6.Triângulo válido:
# Escreva um programa que peça ao usuário para digitar três lados de um triângulo. Verifique se os lados formam um triângulo válido (a soma de dois lados deve ser maior que o terceiro lado).

lado_1 = float(input("Digite o tamanho do lado do triangulo: "))
lado_2 = float(input("Digite o tamanho do lado do triangulo: "))
lado_3 = float(input("Digite o tamanho do lado do triangulo: "))

if lado_1 + lado_2 > lado_3:
    print("O triangulo é valido")
else:
    print("O triangulo é invalido")


# Exercícios com condicionais aninhadas.
# 7.Login simples:
# Crie um sistema de login que peça ao usuário um nome de usuário e uma senha. Se o nome de usuário for "admin" e a senha for "1234", exiba "Login bem-sucedido". Caso contrário, exiba "Credenciais inválidas".

usuario = input("Usuario: ")
senha = (input("Senha: "))

if usuario == "admin" and senha == "12345":
    print("Login bem-sucedido.")
else:
    print("Credenciais invalidas.")


# 8.Cálculo de IMC:
# Peça ao usuário para informar seu peso (em kg) e altura (em metros). Calcule o IMC (Índice de Massa Corporal) e classifique-o:

# Abaixo de 18.5: "Abaixo do peso"

# 18.5 a 24.9: "Peso normal"

# 25 a 29.9: "Sobrepeso"

# 30 ou mais: "Obesidade"

peso = float(input("Digite seu peso em Kg: "))
altura = float(input("Digite sua altura em metros: "))
imc = peso / altura ** 2

if imc > 18.5:
    print("Você está abaixo do peso.")
elif imc > 18.5 and imc <= 24.9:
    print("Você esta com o peso normal.")
elif imc >= 25 and imc <= 29.9:
    print("Você está com sobre peso.")
elif imc >= 30:
    print("Você está com obesidade.")


# Exercícios com condicionais e loops.
# 9.Números divisíveis:
# Use um loop for para iterar sobre os números de 1 a 100. Para cada número, use uma condicional para verificar se ele é divisível por 3, por 5 ou por ambos. Exiba:

# "Divisível por 3" se for divisível por 3.

# "Divisível por 5" se for divisível por 5.

# "Divisível por 3 e 5" se for divisível por ambos.

for numero in range(1, 101):
    if numero % 3 == 0:
        print(f"{numero} é divisível por 3")
    elif numero % 5 == 0:
        print(f"{numero} é divisível por 5")
    elif numero % 3 and numero % 5 == 0:
        print(f"{numero} é divisível por 3 e 5")
    else:
        print(f"{numero} não é divisível por 3 e 5")

# 10.Jogo de adivinhação:
# Crie um jogo em que o programa escolhe um número aleatório entre 1 e 10. Peça ao usuário para adivinhar o número. Use condicionais para informar se o palpite foi alto, baixo ou correto.

import random # Importando o random

numero = random.randint(1, 10)
tentativa = int(input("Chute um numero: "))

if tentativa == numero:
    print("Acertou")
elif tentativa > numero:
    print(f"Chutou alto o numero era: {numero}")
elif tentativa < numero:
    print(f"Chutou baixo o numero era: {numero}")  


"""
Dicas para resolver os exercícios:
Use a função input() para receber entradas do usuário.

Converta as entradas para o tipo adequado (por exemplo, int() ou float()).

Para o exercício 10 (Jogo de adivinhação), use a função random.randint() da biblioteca random para gerar um número aleatório.

Use operadores de comparação (==, !=, >, <, >=, <=) e operadores lógicos (and, or, not) para criar as condições.

Exemplo de solução para o exercício 1 (Positivo, negativo ou zero):
numero = float(input("Digite um número: "))

if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")

Exemplo de solução para o exercício 4 (Classificação de notas):
nota = float(input("Digite uma nota de 0 a 10: "))

if nota >= 7:
    print("Aprovado")
elif nota >= 5:
    print("Recuperação")
else:
    print("Reprovado")
"""
    

