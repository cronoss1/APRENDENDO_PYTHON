# Exercícios com for:
# 1.Contagem regressiva:
# Escreva um programa que use um loop for para imprimir uma contagem regressiva de 10 até 1, e depois imprima "Fogo!".

for contagem in range(10, 0, -1):
    print(contagem)
print("FOGO!")


# 2.Soma de números:
# Crie um programa que use um loop for para calcular a soma de todos os números de 1 a 100.

soma = 0 # inicilizando a variavel soma com 0

# Loop para iterar sobre os numeros de 1 a 100
for numero in range(0, 101):
    soma += numero # Acumula o valor de cada variavel a soma

# Exibe o resultado final
print(f"A soma dos numeros de 1 a 100 é: {soma}")


# 3.Tabuada:
# Peça ao usuário para digitar um número e, usando um loop for, exiba a tabuada desse número de 1 a 10.

numero = int(input("Digite um numero: "))
operadores = input("Qual tabuada, [+], [-], [*], [/]: ")

for loop in range(1, 11):
    if operadores == "+":
        soma = numero + loop
        print(f"{numero} + {loop} = {soma}")
    elif operadores == "-":
        soma = numero - loop
        print(f"{numero} - {loop} = {soma}")
    elif operadores == "*":
        soma = numero * loop
        print(f"{numero} * {loop} = {soma}")
    elif operadores == "/":
        soma = numero / loop
        print(f"{numero} / {loop} = {soma}")


# 4.Números pares:
# Use um loop for para imprimir todos os números pares de 1 a 50.

for loop in range(1, 51):
    if loop % 2 == 0:
        print(f"O numero {loop} é par.")


# 5.Lista de frutas:
# Crie uma lista de frutas (ex.: ["maçã", "banana", "laranja", "uva"]) e use um loop for para imprimir cada fruta da lista.

frutas = ["maçã", "banana", "laranja", "uva"] # Variavel
for lista in frutas: # O codigo sera executado para cada item da sequencia.
    print(lista) # Resultado


# Exercícios com while:
# 6.Adivinhe o número:
# Crie um jogo em que o programa escolhe um número aleatório entre 1 e 100, e o usuário deve adivinhar o número. Use um loop while para continuar pedindo palpites até que o usuário acerte.

import random
# Gera um numero aleatorio de 1 a 100
numero = random.randint(1, 100)
# Loop que continua pedindo palpites até o usuario acertar.
while True:
    tentativa = int(input("Tente acertar o numero de 1 a 100: "))

    if tentativa == numero:
        print("Você acertou!")
        break # Encerra o loop quando o usuario acertar.
    else:
        print("Você errou tente novamente.")


# 7.Soma até digitar zero:
# Escreva um programa que peça ao usuário para digitar números. O loop while deve continuar solicitando números até que o usuário digite 0. Quando isso acontecer, o programa deve exibir a soma de todos os números digitados.

soma = 0 # Iniciliando a variavel soma com 0

while True: # Loop de reptição
    numero = int(input("Digite um numero: ")) # Variavel que recebe os dados
    
    if numero != 0: # Se o numero for defirente de 0, soma com a variavel
        soma += numero
    elif numero == 0: # Se o numero for igual a 0, exibe o soma de todos os numeros anteriores
        print(soma)
        break


# 8.Fibonacci com while:
# Use um loop while para gerar os primeiros 10 números da sequência de Fibonacci (1, 1, 2, 3, 5, 8, 13, 21, 34, 55).

a, b = 1, 1 # Inicializa com os primeiros numeros da sequencia
contador = 0 # Variavel para o numero de repetições

while contador < 10: # Enquanto o numero de repetições for menor do que 10 o loop continuara
    
    print(a, end=" ") # Imprime o resultado (end=" ") faz tudo aparecer em uma unica linha

    a, b = b, a + b # Atribui o valor de (b) a (a) e faz o soma de (a) + (b) e atribui a (b)

    contador += 1 # Adciona uma repetição ao contador 



# Exercícios combinados:
# 9.Números primos:
# Escreva um programa que use um loop for para verificar se um número digitado pelo usuário é primo. Dica: Um número primo é divisível apenas por 1 e por ele mesmo.

numero = int(input("Digite um numero: ")) # Recebe o valor 

if numero > 1: # Verifica se a variavel e maior do que 1
    eh_primo = True # Se for maior que eh_primo e verdadeiro
    
    for divisor in range(2, int((numero**0.5) + 1)): # Calculo da raiz
        if numero % divisor == 0: # Verifica se o resto da divisão é igual a zero
            eh_primo = False # Se for igual a zero então eh_primo é False
            break
    if eh_primo == True: # Se eh_primo continuar como True exibe a mensagem
        print(f"O {numero} é primo")
    else:                # Se eh_primo for False exibe que não é primo 
        print(f"O {numero} não é primo")
else:
    print(f"O numero {numero} não maior que 1, e somente numeros maiores que 1 são primos.")


# 10.Desenho com loops:
# Use loops for aninhados para desenhar um padrão, como um triângulo de asteriscos (*). 
# Por exemplo:
"""
*
**
***    
****
*****
"""
altura = 5 

for linha in range(1, altura + 1): 
    for coluna in range(linha): 
        print("*", end=" ")
    print()