# Exercícios de nível 3:

# EX_11:

idade = int(input("Digite sua idade: "))

if idade >= 18 and idade <= 65:
    print("Você tem idade suficiente para trabalhar aqui.") 
else:
    print("Você não tem idade suficiente para trabalhar aqui.")

# EX_12:

numero = int(input("Digite um número: "))

if numero < 0 or numero > 100:
    print("Número invalido.")
else:
    print("Número valido.")

# EX_13:

semana = "E fim de samana"
semana = not(semana)

if semana == False:
    print("Não é fim de semana")
else:
    print("É fim de semana")

# EX_14:

email = input("Digite seu e-mail: ")

if "@" in email and "." in email:
    print("E-mail valido")
else:
    print("O e-mail não contem @ e .")

# EX_15:
valor_1 = True
valor_2 = True
valor_2 = not(valor_2)

if valor_1 and valor_2 == True:
    print("Ambos os valores são verdadeiros")
elif valor_1 == True or valor_2 == False:
    print("Valor 1 é True e Valor 2 é falso")
elif valor_1 and valor_2 == False:
    print("Ambos os valores são falsos")
elif valor_1 == False or valor_2 == True:
    print("Valor 1 é falso e Valor 2 é verdadeiro")
else:
    print("valor invalido")