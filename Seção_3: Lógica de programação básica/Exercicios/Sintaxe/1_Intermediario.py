# Ex_1: Par ou ímpar com Validação
"""
numero = float(input("Digite um número inteiro: "))

if numero == int(numero):
    if numero % 2 == 0:
        print(f"O número {numero} é par.")
    else:
        print(f"O número {numero} é ímpar.")
else:
    print("Por favor, digite um número inteiro válido.")
"""
# Ex_2: Calculadora com Operações Múltiplas
"""
numero1 = float(input("Digite o primeiro número: "))
operacao = input("Escolha a operação (+, -, *, /, **, %): ")
numero2 = float(input("Digite o segundo número: "))

if operacao == '+':
    resultado = numero1 + numero2
elif operacao == '-':
    resultado = numero1 - numero2
elif operacao == '*':
    resultado = numero1 * numero2
elif operacao == '/':
    if numero2 != 0:
        resultado = numero1 / numero2
    else:
        resultado = "Erro: Divisão por zero."
elif operacao == '**':
    resultado = numero1 ** numero2
elif operacao == '%':
    if numero2 != 0:
        resultado = numero1 % numero2 
    else:
        resultado = "Erro: Divisão por zero."
print(f"O resultado da operação {numero1} {operacao} {numero2} é: {resultado}")
"""
# Ex_3: Maior e Menor em Três

# Ex_4:Conversor de Temperatura

# Ex_5: Número Primo (até 100)

# Ex_6: Tabuada com Escolha

# Ex_7: Contagem Regressiva com (while)

# Ex_8: Conversor de Horas para Minutos e Segundos

# Ex_9: Simulador de Caixa Eletrônica (troco)

# Ex_10: Validador de CPF Simples