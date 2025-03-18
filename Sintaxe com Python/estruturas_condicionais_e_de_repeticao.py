# Indentação e Blocos:
# As linguagens de programação costumam utilizar caracteres ou palavras reservadas para determinar
# o início e fim do bloco. Em Jva e C por exemplo, utilizamos chaves ({}).
# Exemplo:
def sacar(valor): # Início do bloco do método
    saldo = 500

    if saldo >= valor: # Início do bloco do if
        print("Valor sacado!")
    else:
        print("Valor insuficiente!")
    # Fim do bloco do if
# Fim do bloco do método
def depositar(valor):# Início do bloco do método
    saldo = 500
    saldo += valor
# Fim do bloco do método
sacar(500) # Fim do bloco do método

# Estruturas Condicionais:
# A estrutura condicional permite o desvio de fluxo de controle,
# quando determinada expressões lógicas são atendidas.
# Exemplo (if): função (se)
saldo = 2000.0 # Variavel
saque = float(input("Informe o valor de saque: "))

if saldo >= saque: # Se saldo for maior ou igual ao saque (Realiazndo saque!).
    print("Realizando saque!")
if saldo < saque: # Se saldo for menor do que saque (Saldo Insuficiente).
    print("Saldo Insuficiente!")


# Estruturas de Repetição
