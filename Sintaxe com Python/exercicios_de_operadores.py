# Exercícios para aprender tipos de Operadores.

# Exercício_1: Operadores Aritméticos Soma, Subtração, Multiplicação e Divisão:
# Crie um programa que peça dois números ao usuário e exiba o resultado da soma, subtração, multiplicação e divisão desses números.
"""
numero_1 = float(input("Digite um número: "))
operador = input("Qual operação que fazer [+], [-], [*], [/]: ")
numero_2 = float(input("Digite um segundo número: "))
resultado_soma = numero_1 + numero_2
resultado_subtracao = numero_1 - numero_2
resultado_multiplicacao = numero_1 * numero_2
resultado_divisao = numero_1 / numero_2

if operador == "+":
    print(f"A soma de {numero_1} e {numero_1}: {resultado_soma}")
elif operador == "-":
    print(f"A subtração de {numero_1} e {numero_1}: {resultado_subtracao}")
elif operador == "*":
    print(f"A multiplicação de {numero_1} e {numero_1}: {resultado_multiplicacao}")
elif operador == "/":
    print(f"A divisão de {numero_1} e {numero_1}: {resultado_divisao}")
"""

# Exercício_2: Exponenciação e Módulo
# Escreva um programa que calcule a potência de um número elevado a outro e o resto da divisão entre dois números.
"""
numero_1 = int(input("Digite um numero: "))
numero_2 = int(input("Digite mais um numero: "))
elevado = numero_1 ** numero_2
resto_da_divisao = numero_1 // numero_2

print(f"O numero {numero_1} elevado a {numero_2} é: {elevado}")
print(f"O resto da divisão do numero {numero_1} pelo {numero_2} é: {resto_da_divisao}")
"""

# Exercício_3: Divisão Inteira
# Faça um programa que peça dois números e exiba o resultado da divisão inteira entre eles.
"""
numero_1 = int(input("Digite um numero: "))
numero_2 = int(input("Digite mais um numero: "))
divisao = numero_1 / numero_2

print(f"O resultado da dividão de {numero_1} por {numero_2} é: {divisao}")
"""

# Exercício_4: Operadores de Comparação
# Comparação de Números:
# Crie um programa que peça dois números e compare se o primeiro é maior, menor ou igual ao segundo.
"""
numero_1 = int(input("Digite um numero: "))
numero_2 = int(input("Digite mais um numero: "))
    
if numero_1 > numero_2:
    print(f"O numero {numero_1} é maior que o {numero_2}")
elif numero_1 < numero_2:
    print(f"O numero {numero_1} é menor que o {numero_2}")
elif numero_1 == numero_2:
    print(f"O numero {numero_1} é igual ao numero {numero_2}")
"""

# Exercício_5: Verificação de Igualdade:
# Escreva um programa que peça dois valores e verifique se eles são iguais ou diferentes.

# Exercício_6: Operadores de Atribuição, atribuição Simples e Composta:
# Crie um programa que use operadores de atribuição simples (=) e compostos (+=, -=, *=, /=) para modificar o valor de uma variável.

# Exercício_7: Atribuição com Módulo
# Faça um programa que use o operador de atribuição com módulo (%=) para atualizar o valor de uma variável.

# Exercício_8: Operadores Logicos, verificação de Condições:
# Escreva um programa que peça a idade de uma pessoa e verifique se ela é maior de 18 anos e menor de 65 anos.

# Exercício_9: Combinação de Condições
# Crie um programa que peça dois números e verifique se ambos são positivos ou se ambos são negativos.

# Exercício_10: Operadores de Identidade, verificação de Identidade
# Escreva um programa que compare duas variáveis usando is e is not para verificar se elas apontam para o mesmo objeto na memória.

# Exercício_11: Operadores de Associação, verificação de Associação
# Crie um programa que verifique se um determinado elemento está presente em uma lista usando in e not in.

# Exercício_12: Operadores Bitwise, Operações Bitwise
# Escreva um programa que realize operações bitwise (&, |, ^, ~, <<, >>) entre dois números e exiba os resultados.

# Exercício_13: Exercícios Combinados, Calculadora Simples
# Crie uma calculadora simples que permita ao usuário escolher entre diferentes operações (soma, subtração, multiplicação, divisão, exponenciação, etc.) e execute a operação escolhida.

