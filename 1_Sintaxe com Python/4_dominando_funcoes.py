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

# Parâmetros especiais:
"""
Por padrão, argumentos podem ser passados para uma função Python tanto por posição quanto explicitamente pelo nome. 
Para uma melhor legibilidade e desempenho, faz sentido restringir a maneira pelo qual argumentos possam ser passados, 
assim um desenvolvedor precisa apenas olhar para a definição da função para determinar se os itens são passados por posição, 
por posição e nome, ou por nome.
"""
# Exemplo Positional only: 
# Tudo que antes da barra são parâmetros que só podem ser passados por posição
# tudo depois da barra são parâmetros que podem ser Positional ou Keyword
def criar_carro(modelo, ano, placa, /, marca, motor, combustivel): 
    print(modelo, ano, placa, marca, motor, combustivel)


criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  
# válido    Positional only           /       Keyword only

criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") 
# inválido    Keyword only           /        Keyword only

# Exemplo Keyword only:
# Tudo depois do asterisco tem que Keyword only
def criar_carro(*, modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)


criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") 
 # válido    Keyword only

criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  
# inválido   Positional only         /        Keyword only

# Exemplo ibrido Keyword and Positional only:
# Também tem como usar os dois ao mesmo tempo.
def criar_carro(modelo, ano, placa, /, *, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  
# válido     Positional only         /            Keyword only

criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  
# inválido   Keyword only

# Objetos de primeira classe:
"""
Em Python tudo é objeto, dessa forma funções também são objetos o que as tornam objetos de primeira classe. 
Com isso podemos atribuir funções a variáveis, passá-las como parâmetro para funções, usá-las como valores 
em estruturas de dados (listas, tuplas, dicionários, etc) e usar como valor de retorno para uma função (closures).
"""
# Exemplo:
def somar(a, b): # função somar 
    return a + b

def exibir_resultado(a, b, funcao): # acessando a função com a função exibir_resultado
    resultado = funcao(a, b) # Armazenando o resultado na variavel
    print(f"O resultado da operação {a} + {b} = {resultado}")

exibir_resultado(10, 10, somar)  # O resultado da operação 10 + 10 = 20
# Fonecendo os valores

# Escopo local e escopo global
"""
O escopo global é o escopo mais externo de um programa Python. 
Variáveis definidas aqui são acessíveis em qualquer lugar do código.
Variáveis globais são criadas fora de todas as funções
São acessíveis em qualquer função do módulo
Permanecem disponíveis durante toda a execução do programa
"""
# Exemplo:
salario = 2000 # Variável Global

def salario_bonus(bonus): # Função
    global salario # Informando que a variável é global, usar somente quando for necessario
    salario += bonus
    return salario

salario_bonus(500)

# Escopo Local
"""
Definição: O escopo local existe dentro de funções. 
Variáveis definidas aqui só são acessíveis dentro da função onde foram criadas.
Variáveis locais são criadas quando a função é chamada
São destruídas quando a função termina
Não são acessíveis fora da função
"""
# Exemplo:
salario = 2000 # Variável Global

def salario_bonus(bonus): # Função
    global salario  # Informando que a variável e global, usar somente quando for necessario
    salario += bonus # Varável local que somente pode ser usada dento da função
    return salario

salario_bonus(500)
