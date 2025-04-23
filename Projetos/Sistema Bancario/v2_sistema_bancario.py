# Projeto onde estarei criando um sistema bancário com python Versão-02

# Codígo:
def menu():
    menu = """\n
    Qual operação gostaria de fazer:
        [d] Depositar.
        [s] Saque.
        [e] Extrato.
        [nu] Novo usuário.
        [nc] Nova conta.
        [lc] Listar contas.
        [q] Sair.
    
    => """
    return input(menu) # Variável menu, responsavel pelas opções que podemos escolher

# Função depositar:
def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"+++ Depósito de R$ {valor:.2f} realizado com sucesso! +++")
    else:
        print("@@@ Operação falhou! O valor informado é inválido. @@@")
    return saldo, extrato


def sacar(saldo, valor, extrato, limite, numero_saques, limite_saque):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saque

    if excedeu_saldo:
        print("@@@ Operação falhou! Você não tem saldo suficiente. @@@")

    elif excedeu_limite:
        print("@@@ Operação falhou! Você execedeu o valor limite. @@@")

    elif excedeu_saques:
        print("@@@ Operação falhou! Você atingiu o limite de saques. @@@")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("+++ Saque realizado com sucesso! +++")
    return saldo, extrato, numero_saques


def exibir_extrato(saldo, extrato):
    print("\n===============EXTRATO===============")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\n Saldo: R$ {saldo:.2f}")
    print("=====================================")


def criar_usuario(usuarios):
    cpf = int(input("Informe o CPF (digite apenas números): "))
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n @@@ Já existe usuário com esse CPF! @@@")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaa): ")
    endereco = input("Informe o endereço (logradouro, numero - barrio - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("+++ Usuário criado com sucesso! +++")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def main():
    LIMITE_SAQUE = 3
    numero_saques = 0

    saldo = 0
    limite = 500
    extrato = ""

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Digite o valor do depósito: R$ "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Digite o valor do saque: R$ "))

            saldo, extrato, numero_saques= sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saque=LIMITE_SAQUE,
            )
        elif opcao == "e":
            print(exibir_extrato(saldo, extrato=extrato))
            
        elif opcao == "q":
            break

        else:
            print("@@@Operação invalida, por favor selecione novamente a operação desejada.@@@")

main()