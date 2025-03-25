# O que são funções?
"""
Funções em Python são blocos de código reutilizáveis que realizam uma tarefa específica. 
Elas são fundamentais para organizar e estruturar programas, permitindo:
"""
# 1. Função sem parâmetros:
# (def) inicia a definição de uma função
# ( () ) parenteses vazios indicam que a função não recebe parâmetros
def exibir_mensagem(): # (exibir_mensagem) nome da função
    print("olá mundo!") # Corpo da função (o que ela executa)

# 2. Função com Parâmetro Obrigatório
# (nome) Parâmetro obrigatório (deve ser fornecido na chamada)
def exibir_mensagem_2(nome): 
    print(f"Seja bem vindo {nome}!") # f-string: f"..." permite interpolação de variáveis (insere o valor de nome no texto)

# 3. Função com Parâmetro Opcional (valor padrão)
# nome="Ricardo": Parâmetro com valor padrão (opcional)
# Se nenhum valor for fornecido usa "Ricardo"
def exibir_mensagem_3(nome="Ricardo"): # Valor padrão
    print(f"Seja bem vindo {nome}")

exibir_mensagem() # Executa a função
exibir_mensagem_2(nome="Kauã") # (nome="Kauã") passa o valor "Kauã" para o parâmetro nome
exibir_mensagem_3() # Sem argumento -> usa valor padrão -> "Seja bem vindo Ricardo"
exibir_mensagem_3(nome="Chapolim") # Fornece valor -> "Seja bem vindo Chapolim"

# Retornando Valores:
"""
Para retornar um valor, utilizamos a palavra reservada return.
Toda função Python retorna None por padrão. Diferente de outras 
linguagens de programação, em Python uma função pode retornar mais 
de um valor.
"""
# Exemplo:
def calcular_total(numeros): # Recebe uma lista de numeros 
    return sum(numeros) # (sum) para soma todos os elementos da lista

def retorna_antecessor_e_sucessor(numero): # Recebe um numero como padrão
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor

print(calcular_total([10, 20, 35])) # exibe o resultado
print(retorna_antecessor_e_sucessor(15)) # exibe o resultado

# Argumentos nomeados: 
"""
Funções também podem ser chamadas usando argumentos
nomeados da forma chave=valor."
"""
# Exemplo:
def salvar_carro(marca, modelo, ano, placa):
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

salvar_carro("Fiat", "Palio", 2000, "ABC-123")
salvar_carro(marca="Fiat", modelo="Palio", ano="2000", placa="ABC-123")
salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 2000, "placa": "ABC-123"})
# Passando um dicionario usando (**) para passar esse valores.

