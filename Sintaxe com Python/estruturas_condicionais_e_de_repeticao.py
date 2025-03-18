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

# Exemplo (if): Função (if/se)
saldo = 2000.0 # Variavel
saque = float(input("Informe o valor de saque: "))

if saldo >= saque: # Se saldo for maior ou igual ao saque (Realiazndo saque!).
    print("Realizando saque!")
if saldo < saque: # Se saldo for menor do que saque (Saldo Insuficiente).
    print("Saldo Insuficiente!")

# Exemplo (if/else): Função (if/se e else/ se não)
saldo = 2000.0 # Variavel
saque = float(input("Informe o valor de saque: "))

if saldo >= saque: # Se saldo for maior ou igual ao saque (Realiazndo saque!).
    print("Realizando saque!")
else: # Se não atender ao requisito do if executa o else (Saldo Insuficiente).
    print("Saldo Insuficiente!")

# Exemplo (if/elif/else): Função (if/se, elif/se não se, elif/se não)
opcao = int(input("Informe uma opção: [1] Sacar \n[2] Extrato: "))

if opcao == 1:
    valor = float(input("Informe a quantia para o saque: "))
elif opcao == 2:
    print("Exibindo o extrato...")
else:
    print("Opção inválida")

# Estruturas de Repetição
# São estruturas utilizadas para repetir um trecho de código um determinado número de vezes.
# Esse número pode ser conhecido previamente ou determinado através de uma expressão lógica.
# Exemplo (for): E usado quando sabemos o número exato de vezes que nosso bloco de código
# deve ser executado.
texto = input("Informe um texto:") # Variavel
VOGAIS = "AEIOU" # Laço de repetição

for letra in texto:
    # Transformando letra para maiusculo.
    if letra.upper() in VOGAIS:
        print(letra, end="") # adiciona uma quebra de linha
print()

# Exemplo (for/else): else executa depois do laço de repetição
texto = input("Informe um texto:") # Variavel
VOGAIS = "AEIOU" # Laço de repetição

for letra in texto:
    # Transformando letra para maiusculo.
    if letra.upper() in VOGAIS:
        print(letra, end="") # adiciona uma quebra de linha
else:
    print("Executado depois do laço")

# Exemplo (range): Usado para produzir uma sequência de números.
