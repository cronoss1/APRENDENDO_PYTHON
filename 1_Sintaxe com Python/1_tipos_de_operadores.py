# Operadores aritmeticos
"""
# Adição
print( 2 + 3)

# Subtração
print(5 - 3)

# Multplicação
print(3 * 5)

# Divisão
print(8 / 2)

# Divisão Inteira
print(12 // 2) # Retorna apenas um número inteiro

# Modulo
print(10 % 3) # Retorna o resto da divisão

# Exponenciação
print(2 ** 3)
"""
# Exemplo:
produto_1 = 25
produto_2 = 12

print(produto_1 + produto_2)
print(produto_1 - produto_2)
print(produto_1 / produto_2)
print(produto_1 // produto_2)
print(produto_1 * produto_2)
print(produto_1 % produto_2)
print(produto_1 ** produto_2)

x = (10 + 5) * 4 # Os parênteses podem ser usados para definir a ordem de operações
y = (10 * 2) + 10 - (25) # Os parênteses são usados para definir a prioridade

print(x)
print(y)

# Operadores de Comparação
"""
Operadores de comparação (relacionais)
OP           Siginificado         Exemplo(True)
>             Maior                2 > 1
>=            Maior ou igual       2 >= 1
<             Menor                1 < 2
<=            Menor ou igual       2 <= 1
==            Igual               'a' == 'a'
!=            Diferente           'a' != 'b'  
"""
#Exemplo:
maior = 2 > 1
maior_ou_igual = 2 >= 2
menor = 1 < 2
menor_ou_igual = 1 <= 1
igual = 'a' == 'a'
diferente = 'a' != 'b'
print(diferente)

# Operadores de Atribuição
# =    Atribuição
# +=   Adição 
# -=   Subtração
# *=   Multiplicação
# /=   Divisão
# //=  Divisão Inteira
# **=  Exponenciação
# %=   Modulo (Resto da Divisão)

# Exemplo: 
numero = 10
numero += 5

print(numero)

# Operadores de Logicos
"""
and ->(e) or ->(ou) not ->(não)
and -> Todas as condições precisam ser verdadeiras.
Se qualquer valor for considerado falso, a expressão
inteira será avaliada naquele valor.
São considerados falsy (que você já viu)
0 0.0 '' False
Também existe o tipo None que é usado para representar um não valor
"""
# and = Para ser True tudo tem que ser True
# or = para ser True apenas um tem que ser True

#Operador Logico (and):
#Exemplo and:
entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '12345'
#Exemplo and:
if entrada == 'E'and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')
#Avaliação de curto circuito
print(True and False and True)

#Operador Logico (or):
#Exemplo or:
entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '12345'

#Exemplo or:
if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')

#Avaliação de curto circuito:
senha = 0 or False or 0 or 'abc' or True
print(senha)

#Operador lógico "not"
#Usado para inverter expressões
#not True = False
#not False = True

#Exemplo:
#print(not True) #False
#print(not False) #True

"""
Operadores in e not in
in -> (está entre)
not in -> (não está entre)
Strings são iteráveis
 0 1 2 3 4 5 -> ìndice
 O t á v i o
-6-5-4-3-2-1
"""

#Exemplo in/not in:
"""in
nome = 'Otávio'
print(nome[2])
print(nome[-4])

print('á' in nome)
print('vio' in nome)
print('zero' in nome)
print(10 * '-')
print('vio' not in nome)
print('zero' not in nome)
"""
#Exemplo in/not in:
nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')

# Operadores de Identidade
# São operarodes utilizados para comparar se os dois objetos testados ocupam a mesma região na memoria
# Operador (is) e (is not)
saldo = 1000
limite = 1000

print(saldo is limite) # Se ocupam a mesma região (True)
print(saldo is not limite) # Se não ocupam a mesma região (False)

# Operadores de Associação
# São operadores utilizados para verificar se um objeto está presente em uma sequência.
# Operador (in) Verificar se está na lista ou variavel
# Operador (not in) Verificar se não está na lista ou variavel
frutas = ["limão", "manga", "laranja"] 

print("manga" in frutas)
print("uva" not in frutas)
