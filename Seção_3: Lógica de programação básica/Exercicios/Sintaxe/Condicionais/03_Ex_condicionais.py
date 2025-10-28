# Exercícios de nível 3:

# EX_11:
"""
nota = float(input("Digite a nota do aluno: "))

if nota >= 5:
    if nota >= 9:
        print("Aluno tirou nota A")
    elif nota >= 7:
        print("Aluno tirou nota B")
    elif nota >= 5:
        print("Aluno tirou nota C")
else:
    print("Aluno reprovado")
"""
# EX_12:
"""
peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))
imc = peso / (altura ** 2)

if imc >= 18.5:
    if imc >= 30 and imc <= 34.9:
        print(f"Você tem um imc de {imc:.2f}, obesidade tipo 1 ")
    elif imc >= 25 and imc <= 29.9:
        print(f"Você tem um imc de {imc:.2f}, sobrepeso")
    elif imc >= 18.5 and imc <= 24.9:
        print(f"Você tem um imc de {imc:2f}, peso normal")
else:
    print(f"Você tem um imc de {imc:.2f}, abaixo do peso")
"""
# EX_13:
"""
dia = int(input("Digite o dia da semana: "))

if dia > 1 and dia < 7:
    print("Dia util")
elif dia == 1 or dia == 7:
    print("Final de semana")
else:
    print("Dia invalido")
""" 
# EX_14:
# isdigit é um método que retorna True se o caractere for um número (0-9)
# isalpha retorna True se o caractere for letra (a-z ou A-Z)
senha = input("Digite a senha: ")

def senha_e_valida(senha):
    # 1° Verifica o tamanho mínimo
    if len(senha) < 8:
        return False  # Senha muito curta!
    
    achou_numero = False
    achou_letra = False
    
    # 2° Analisa cada caractere
    for letra_ou_numero in senha:
        if letra_ou_numero.isnumeric():  # É um número?
            achou_numero = True
        elif letra_ou_numero.isalpha():  # É uma letra?
            achou_letra = True
    
    # 3° Retorna True somente se atender tudo
    return achou_numero and achou_letra
if senha_e_valida(senha):
    print("Senha válida")
else:
    print("Senha inválida")
# EX_15:
