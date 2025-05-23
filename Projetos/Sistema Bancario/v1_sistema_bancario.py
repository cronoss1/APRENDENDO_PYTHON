# Projeto onde estarei criando um sistema bancário com python 

# Codígo:
menu = """
Qual operação gostaria de fazer:
    [d] Depositar.
    [s] Saque.
    [e] Extrato.
    [q] Sair.

=> """ # Variável menu, responsavel pelas opções que podemos escolher

saldo = 0 # Variável do saldo da conta 
limite = 500 # Variável de limite de saque
extrato = "" # Variável de extrato da conta 
numero_saques = 0 # Variável que armazena o numero de saques feitos
LIMITE_SAQUE = 3 # Constante recebe um valor de limite de saque diario, que não deve ser mudado

while True: # Laço de repetição que ira executar a operação enquanto for verdadeiro.
    opcao = input(menu) # Executa a variável menu

    if opcao == "d": # Verifica se escolhemos a opção deposito, excuta o código abaixo
        valor = float(input("Digite o valor do deposito: ")) # Variável que recebe o valor de deposito
        if valor > 0: # Se o valor for maior que zero executa os códigos abaixo
            saldo += valor # Operação onde o saldo recebe o valor depositado
            extrato += f"Depósito: R$ {valor:.2f}\n" # Extrato recebe a movimentação de deposito
            print("Deposito efetuado com sucesso.") # Mensagem de que a operação foi realizada com sucesso.
        else: # Se o valor que deseja depositar for menor que zero executa a código 
            print("Operação falhou! Valor informado inválido.")

    elif opcao == "s": # Verifica se escolhemos  a opção saque, executa o código abaixo
        if numero_saques != LIMITE_SAQUE: # Verifica se o numero de saques é diferente do limite de saque.
            saque = float(input("Digite o valor de saque: ")) # Variável que o valor de saque
            if saque <= saldo: # Se o valor de saque for menor ou igual ao de saldo executa os códigos abaixo.
                if saque <= limite: # Se o valor de saque for menor ou igual ao valor limite de saque,
                    # os códigos abaixo.
                    saldo -= saque # Operação que retira o valor que sera sacado da variável saldo
                    numero_saques += 1 # Operação que adiciona 1 ao numero de saques realizados
                    extrato += f"Saque: R$ {saque:.2f}\n" # Extrato recebe a movimentação de saques
                    print("Saque efetuado com sucesso.") # Mensagem de que a operação foi realizada com sucesso.
                else: # Se o valor que deseja sacar for maior que o valor limite, executa o código abaixo
                    print("Valor de saque muito alto!")
            else: # Se o valor que deseja sacar for maior que o saldo, executa o código abaixo.
                print("Saldo insuficiente.")
        else: # Se tentar sacar depois de atingir o limite maximo de saques diários, executa o código abaixo.
            print("Você atingiu seu limite diario de saque.")
    
    elif opcao == "e": # Verifica se escolhemos a opção extrato, excuta o código abaixo.
        print("\n===============EXTRATO===============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        # Se a variável extrato estiver varias ira mostrar a mensagem, se não ira mostrar as movimentações
        # em extrato.
        print(f"\nSaldo: R$ {saldo:.2f}") # Mostra o saldo atual da conta.
        print("=======================================")

    elif opcao == "q": # Verifica se escolhemos a opção sair.
        print("Sair") # Mostra a mensagem sair na tela
        break # Encerra o loop caso escolhemos a opção [q] Sair.
    
    else: # Executa caso escolhemos alguma opção diferente das que estão em menu.
        print("Operação inválida, por favor selecione novamente a opção desejada.")
