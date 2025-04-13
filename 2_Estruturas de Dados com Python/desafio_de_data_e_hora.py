# Introdução:
"""
Com os novos conhecimentos adquiridos sobre data e hora, você foi encarregado de 
implementar as seguintes funcionalidades no sisetma:
- Estabelecer um limite de 10 transações diárias para uma conta
- Se o usuário tentar fazer uma transação após atingir o limite, deve ser informado 
  que ele excedeu o número de transações permitidas para aquele dia.
- Mostre no extrato, a data e hora de todas as transações.
"""
# Codígo:
import textwrap 
# textwrap: usado para manipular e formatar blocos de texto com indentação e quebra de linha
from abc import ABC, abstractclassmethod, abstractproperty 
# permite criar classes abstratas (com métodos que precisam ser implementados nas subclasses) 
# ABC: classe base para criar classes abstratas
# abstractlassmethod: força implementação de métodos de classe
# abstractproperty: força implementação de propriedades
from datetime import datetime # pega data e hora atual, pode ser usado para registrar transações

# Define uma classe que implementa um iterador personalizado para contas (permite iterar com for in contas)
class ContasIterador:
    # Função init, construtor que recebe uma lista de contas
    def __init__(self, contas):
        self.contas = contas # armazena essa lista de contas
        self._index = 0 # Controla a posição atual do iterador (inicia em 0)

    def __iter__(self): # retorna o próprio objeto, pois ele é um iterador.
        return self

    def __next__(self): # método que retorna o próximo item da iteração
        try: # Tenta acessar (conta) pelo índice atual.
            conta = self.contas[self._index]
             # Retorna uma string formatada com os dados da conta:
            return f"""\
            Agência:\t{conta.agencia}
            Número:\t\t{conta.numero}
            Titular:\t{conta.cliente.nome}
            Saldo:\t\tR$ {conta.saldo:.2f}
        """
        # Se o índice for maior do que a quantidade de contas, levanta o erro StopIteration, que indica o fim da iteração
        except IndexError:
            raise StopIteration
        finally: # Independente de sucesso ou erro, incrementa o índice para o próximo elemento.
            self._index += 1

# Representa os usuários
class Cliente:
    # Função __init__: Construtor da classe Cliente, que inicializa:
    def __init__(self, endereco):
        self.endereco = endereco # o endereço do cliente
        self.contas = [] # uma lista vazia para armazenar as contas do cliente
        self.indice_conta = 0 # variável para controle do índice da conta, que começa em 0

    # Função realizar_transacao: Método que recebe uma conta e uma transacao (por exemplo, saque ou depósito).
    def realizar_transacao(self, conta, transacao):
        # Ele apenas chama o método registrar da transação, que executa a operação (depósito ou saque) na conta.
        # TODO: validar o número de transações e invalidar a operação se for necessário
        # print("\n@@@ Você excedeu o número de transações permitidas para hoje! @@@")
        transacao.registrar(conta)

    # Função adicionar_conta: Método que adiciona uma nova conta à lista de contas do cliente.
    def adicionar_conta(self, conta):
        self.contas.append(conta)

# Representa os usuários
class PessoaFisica(Cliente): # PessoaFisica: Herda de Cliente, mas adiciona:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco) # Chama o construtor da classe base (Cliente), inicializando o endereço.
        self.nome = nome #  nome da pessoa.
        self.data_nascimento = data_nascimento # data de nascimento.
        self.cpf = cpf # CPF da pessoa.

# Representa contas bancárias
class Conta:
    # Função __init__: Construtor da classe Conta, que recebe:
    def __init__(self, numero, cliente): 
        # numero: número da conta.
        # cleinte: objeto do tipo Cliente (ou suas subclasses, como PessoaFisica).
        self._saldo = 0 # o saldo da conta começa com 0.
        self._numero = numero # o número da conta.
        self._agencia = "0001" # a agência é fixa como "0001".
        self._cliente = cliente # armazena o cliente associado à conta.
        self._historico = Historico() # um objeto de Historico para registrar transações.

    # Funcção nova_conta: Método de classe que cria uma nova conta e retorna uma 
    # instância da classe Conta com os parâmetros fornecidos.
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    # Função saldo: Propriedade que retorna o saldo atual da conta.
    @property
    def saldo(self):
        return self._saldo

    # Função numero: Propriedade que retorna o número da conta
    @property
    def numero(self):
        return self._numero

    # Função agencia: Propriedade que retorna a agência da conta.
    @property
    def agencia(self):
        return self._agencia

    # Função cliente: Propriedade que retorna o cliente associado à conta.
    @property
    def cliente(self):
        return self._cliente

    # Função historico: Propriedade que retorna o histórico de transações da conta.
    @property
    def historico(self):
        return self._historico

    # Função sacar: Método para realizar um saque na conta.
    def sacar(self, valor): # Verifica se o valor solicitado é maior que o saldo disponível.
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        # Se o valor for válido, diminui o saldo e retorna True, caso contrário, retorna False.
        if excedeu_saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

        elif valor > 0:
            self._saldo -= valor
            print("\n=== Saque realizado com sucesso! ===")
            return True

        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

        return False

    # Função depositar: Método para realizar um depósito na conta.
    def depositar(self, valor): 
        # Verifica se o valor do depósito é positivo e, se for, aumenta o saldo e retorna True. 
        # Caso contrário, retorna False.
        if valor > 0:
            self._saldo += valor
            print("\n=== Depósito realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False

        return True

# Representa contas bancárias
class ContaCorrente(Conta): # ContaCorrente: Herda de Conta e adiciona mais atributos:
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        # super().__init__(numero, cliente): Chama o construtor de Conta.
        super().__init__(numero, cliente)
        self._limite = limite # limite: limite de saldo disponível para saque.
        self._limite_saques = limite_saques # limite_saques: número máximo de saques por dia.

    # Função nova_conta: Método de classe para criar uma nova conta corrente com limites 
    # específicos de saque e saldo.
    @classmethod
    def nova_conta(cls, cliente, numero, limite, limite_saques):
        return cls(numero, cliente, limite, limite_saques)

    # Função sacar: Sobrescreve o método sacar da classe Conta:
    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )
        # Verifica se o valor do saque excede o limite da conta.
        excedeu_limite = valor > self._limite
        # Verifica se o número de saques já atingiu o limite diário.
        excedeu_saques = numero_saques >= self._limite_saques

        if excedeu_limite: 
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

        elif excedeu_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

        else: # Se tudo estiver dentro dos limites, chama o método sacar da classe base.
            return super().sacar(valor)

        return False
    
    # Função __str__: Define uma representação em string para a conta corrente, 
    # formatando os dados de maneira legível.
    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """

# Guarda as transações feitas na conta
class Historico:
    # Função __init__: Construtor da classe Historico, que inicializa:
    def __init__(self):
        self._transacoes = [] # self._transacoes: uma lista vazia para armazenar o histórico das transações.

    # Função transacoes: Propriedade que retorna a lista de transações realizadas.
    @property
    def transacoes(self):
        return self._transacoes

    # Função adicionar_transacao: Método que adiciona uma transação ao histórico.
    def adicionar_transacao(self, transacao): # Ele cria um dicionário com as seguintes informações:
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__, # nome da classe da transação (como Saque ou Deposito).
                "valor": transacao.valor, # valor da transação.
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"), # data e hora da transação no formato dd-mm-aaaa hh:mm:ss.
            }
        )

    # gerar_relatorio: Método que gera um relatório de transações.
    def gerar_relatorio(self, tipo_transacao=None): # Se tipo_transacao for None, ele retorna todas as transações.
        for transacao in self._transacoes:
            if tipo_transacao is None or transacao["tipo"].lower() == tipo_transacao.lower():
                yield transacao 

    # TODO: filtrar todas as transações realizadas no dia
    # transacoes_do_dia: Método que poderia ser usado para filtrar as transações realizadas no mesmo dia. 
    # No entanto, ele ainda está sem implementação (comentado como "TODO").
    def transacoes_do_dia(self):
        pass

# Sistema de transações
class Transacao(ABC):# Transacao: Classe abstrata que serve como base para transações específicas (como Saque e Deposito).
    @property
    @abstractproperty
    def valor(self): # Uma propriedade abstrata que deve ser implementada nas subclasses para obter o valor da transação.
        pass

    @abstractclassmethod
    def registrar(self, conta): # Método abstrato que deve ser implementado nas subclasses para registrar a transação na conta.
        pass

# Sistema de transações
class Saque(Transacao): # Saque: Classe que representa uma transação de saque. Ela herda de Transacao.
    # __init__: Construtor que recebe o valor do saque e o armazena em self._valor.
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self): # Propriedade que retorna o valor do saque.
        return self._valor

    # registrar: Método que registra o saque na conta.
    def registrar(self, conta): # Chama o método sacar da conta.
        sucesso_transacao = conta.sacar(self.valor)

        # Se o saque for realizado com sucesso, a transação é adicionada ao histórico da conta.
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

# Sistema de transações
class Deposito(Transacao): # Classe que representa uma transação de depósito. Ela também herda de Transacao.
    # __init__: Construtor que recebe o valor do depósito e o armazena em self._valor.
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self): # Propriedade que retorna o valor do depósito.
        return self._valor

    # Método que registra o depósito na conta.
    def registrar(self, conta): # Chama o método depositar da conta.
        sucesso_transacao = conta.depositar(self.valor)
         
        # Se o depósito for realizado com sucesso, a transação é adicionada ao histórico da conta.
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

# Decorator que loga data e hora de funções
def log_transacao(func):
    def envelope(*args, **kwargs):
        resultado = func(*args, **kwargs)
        print(f"{datetime.now()}: {func.__name__.upper()}")
        return resultado

    return envelope

# Exibe o menu principal.
def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))

# Busca um cliente pelo CPF.
def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None


# Retorna a primeira conta do cliente (FIXME: não permite escolher se houver mais de uma).
def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\n@@@ Cliente não possui conta! @@@")
        return

    # FIXME: não permite cliente escolher a conta
    return cliente.contas[0]


# Função com input do usuário que executa ações na conta usando Transacao.
@log_transacao
def depositar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)


# Função com input do usuário que executa ações na conta usando Transacao.
@log_transacao
def sacar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)


# Função com input do usuário que executa ações na conta usando Transacao.
@log_transacao
def exibir_extrato(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    print("\n================ EXTRATO ================")
    extrato = ""
    tem_transacao = False
    for transacao in conta.historico.gerar_relatorio():
        tem_transacao = True
        extrato += f"\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}"

    if not tem_transacao:
        extrato = "Não foram realizadas movimentações"

    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
    print("==========================================")


# Cria objetos de cliente e conta e adicionam às listas.
@log_transacao
def criar_cliente(clientes):
    cpf = input("Informe o CPF (somente número): ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("\n@@@ Já existe cliente com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)

    clientes.append(cliente)

    print("\n=== Cliente criado com sucesso! ===")


# Cria objetos de cliente e conta e adicionam às listas.
@log_transacao
def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado, fluxo de criação de conta encerrado! @@@")
        return

    # NOTE: O valor padrão de limite de saques foi alterado para 50 saques
    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta, limite=500, limite_saques=50)
    contas.append(conta)
    cliente.contas.append(conta)

    print("\n=== Conta criada com sucesso! ===")


# Usa ContasIterador para mostrar todas as contas.
def listar_contas(contas):
    for conta in ContasIterador(contas):
        print("=" * 100)
        print(textwrap.dedent(str(conta)))


# Loop principal da aplicação, guarda a lista de clientes e contas.
def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            depositar(clientes)

        elif opcao == "s":
            sacar(clientes)

        elif opcao == "e":
            exibir_extrato(clientes)

        elif opcao == "nu":
            criar_cliente(clientes)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("\n@@@ Operação inválida, por favor selecione novamente a operação desejada. @@@")


main()