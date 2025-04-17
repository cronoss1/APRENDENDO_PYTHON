# # Projeto onde estarei criando um sistema bancário com python Versão-02
"""
Objetivo Geral:
Separar as funções existentes de saque, depósito e extrato em funções específicas.
Criar duas novas funções: cadastrar usuário(cliente) e criar conta.
"""
"""
Desafio:
Precisamos deixar nosso código mais modularizado, para isso vamos criar funções para as operações
existentes: sacar, depositar e extrato. Além disso, vamos criar duas novas funções: cadastrar usuário(cliente)
e criar conta.
"""
"""
Separação em funções:
Devemos criar funções para cada operação existente. Para exercitar tudo o que aprendemos até agora,
cada função vai ter uma regra na passagem de argumentos.
"""
"""
Saque:
A função saque deve receber os argumentos apenas por nome (keyword only).
Sugestão: saldo, valor, extrato, limite, numero_saques, limite_saque.
Sugestão de retorno: saldo, extrato, numero_saques.
"""
"""
Depósito:
A função depósito deve receber os argumentos apenas por posição (positional only).
Sugestão: saldo, valor, extrato.
Sugestão de retorno: saldo, extrato.
"""
"""
Extrato:
A função extrato deve receber os argumentos por posição e nome (keyword only e positional only).
Argumentos posicionais: saldo.
Argumentos nomeados: extrato.
"""
"""
Novas Funções:
Precisamos criar duas novas funções: cadastrar usuário(cliente) e criar conta.
Fique a vontade para criar mais funções exemplo: listar contas.
"""
"""
Criar usuário(cliente):
O programa deve armazenar os usuários em uma lista, um usuário é composto por: nome, data de nascimento,
CPF e endereço. O endereço é uma string com o formato: logradouro, numero - bairro - cidade/estado.
Deve ser armazenado somente os números do CPF. Não podemos cadastrar 2 usuários com o mesmo CPF.
"""
"""
Criar conta:
O programa de armazena as contas em uma lista, uma conta é composta por: número da conta, agência e usuário.
O número da conta é sequencial, iniciando em 1. O número da agência é fixo, por exemplo: 0001.
O usuário pode ter mais de uma conta, mas uma conta só pode ter um usuário.
"""
"""
Dica:
Para Vincular um usuário a uma conta, filtre a lista de usários buscando o número do CPF informado
para cada usuário da lista.
"""
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