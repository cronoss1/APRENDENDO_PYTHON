"""
Flag (Bandeira) - Marca um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade
"""
v1 = "a"
print(id(v1)) # ve a identidade do elemento na memoria

condicao = False
passou_no_if = None # Variavel definida com valor None

if condicao:
    passou_no_if = True
    print("Faça algo")
else: 
    print("Não faça algo")

if passou_no_if is None:
    print("Não passou no if")
else:
    print("Passou no if")

# Exercicios_1:
"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero = int(input("Digite um número inteiro: "))

if numero == int:
    if numero % 2 == 0:
        print(f"O número {numero} é par.")
    else:
        print(f"O número {numero} é impar")
else:
    print("Você não digitou um número inteiro.")


# Exercicios_2:
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""


# Exercicios_3:
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
