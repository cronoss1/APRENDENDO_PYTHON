# Exercícios com (if) básico.
# 1.Positivo, negativo ou zero:
# Escreva um programa que peça ao usuário para digitar um número e determine se ele é positivo, negativo ou zero.

# 2.Maior de idade:
# Peça ao usuário para informar sua idade. Se a idade for maior ou igual a 18, exiba "Você é maior de idade". Caso contrário, exiba "Você é menor de idade".

# 3.Par ou ímpar:
# Crie um programa que verifique se um número digitado pelo usuário é par ou ímpar. Dica: Use o operador % (resto da divisão).

# Exercícios com (if-else) e (elif).
# 4.Classificação de notas:
# Peça ao usuário para digitar uma nota de 0 a 10. Classifique a nota da seguinte forma:

# 0 a 4: "Reprovado"

# 5 a 6: "Recuperação"

# 7 a 10: "Aprovado"

# 5.Comparação de números:
# Peça ao usuário para digitar dois números. Exiba uma mensagem informando qual número é maior ou se eles são iguais.

# 6.Triângulo válido:
# Escreva um programa que peça ao usuário para digitar três lados de um triângulo. Verifique se os lados formam um triângulo válido (a soma de dois lados deve ser maior que o terceiro lado).

# Exercícios com condicionais aninhadas.
# 7.Login simples:
# Crie um sistema de login que peça ao usuário um nome de usuário e uma senha. Se o nome de usuário for "admin" e a senha for "1234", exiba "Login bem-sucedido". Caso contrário, exiba "Credenciais inválidas".

# 8.Cálculo de IMC:
# Peça ao usuário para informar seu peso (em kg) e altura (em metros). Calcule o IMC (Índice de Massa Corporal) e classifique-o:

# Abaixo de 18.5: "Abaixo do peso"

# 18.5 a 24.9: "Peso normal"

# 25 a 29.9: "Sobrepeso"

# 30 ou mais: "Obesidade"

# Exercícios com condicionais e loops.
# 9.Números divisíveis:
# Use um loop for para iterar sobre os números de 1 a 100. Para cada número, use uma condicional para verificar se ele é divisível por 3, por 5 ou por ambos. Exiba:

# "Divisível por 3" se for divisível por 3.

# "Divisível por 5" se for divisível por 5.

# "Divisível por 3 e 5" se for divisível por ambos.

# 10.Jogo de adivinhação:
# Crie um jogo em que o programa escolhe um número aleatório entre 1 e 10. Peça ao usuário para adivinhar o número. Use condicionais para informar se o palpite foi alto, baixo ou correto.

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
    

