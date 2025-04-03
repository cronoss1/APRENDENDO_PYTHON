# Conhecendo métodos úteis da classe string
curso = " pYtHon "

print(curso.upper())  # Converte todos os caracteres para maiusculo
print(curso.lower())  # Converte todos os caracteres para minusculo
print(curso.title())  # Converte todos os caracteres para minusculo exceto o primeiro 

print(curso.strip())  # Remove todos os espaços em branco 
print(curso.lstrip()) # Remove os espaços em branco da esquerda
print(curso.rstrip()) # Remove os espaços em branco da direita

print(curso.center(10, "#")) # O numero de caracteres que sera usado para centralizar
print(".".join(curso))       # Junta o caracter junto com a string

# Em Python temos 3 formas de interpolar variáveis em strings, a primeira é usando o sinal (%),
# a sengunda é utilizando o método (format) e a última é utilizando (f-strings).

# 1. Old style %: 
# Exemplo:

nome = "Gustavo"
idade = 25
profissao = "programador"
linguagem = "Python"

print("Olá, me chamdo %s. Eu tenho %d anos de idade, trabalho como %s e estou"
" matriculado no curso de %s." % (nome, idade, profissao, linguagem))

# 2. Metodo format:
# Exemplo:

nome = "Gustavo"
idade = 25
profissao = "programador"
linguagem = "Python"

print("Olá, me chamdo {}. Eu tenho {} anos de idade, trabalho como {} e estou"
" matriculado no curso de {}.".format(nome, idade, profissao, linguagem))

# 3. f-string:
# Exemplo:

nome = "Gustavo"
idade = 25
profissao = "programador"
linguagem = "Python"

print(f"Olá, me chamdo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou"
f" matriculado no curso de {linguagem}.")

# Fatiamento de strings é uma técnica utilizada para retornar substrings (partes da string original),
# informando (start), fim(stop) e passo (step): [start:stop[,step]].
# Fatiamento de strings:
# Exemplo:
nome = "Gustavo lopes silva"
#       0123456789123456789
print(nome[0]) # Pega o índice 0

print(nome[:9]) # Pega o índice 0 até o 9

print(nome[10:]) # Pega do índice 10 até o ultimo índice

print(nome[10:16]) # Pega do 10 até o 16

print(nome[10:16:2]) # Pega do 10 até 16 no intervalo de 2 caracteres

print(nome[:]) # Vai do primeiro até o ultimo índice

print(nome[::-1]) # Pega do ultimo índice até o primeiro 

# Strings múltiplas linhas: Strings de mpultiplas linhas são definidas informando 3 aspas simples
# ou duplas durante a atribuição. Elas podem ocupar varias linhas do código, e todos os espaços 
# em branco são incluídos na string final.
 # Exemplo:
nome = "Kauã"
# Ela preserva a formatação da string ao exibir 
mensagem = f"""
Olá meu nome é {nome},
 Eu estou aprendendo Python
""" 
print(mensagem) 

nome = "Kauã"

mensagem = f'''
Olá meu nome é {nome},
 Eu estou aprendendo Python
'''
print(mensagem)
 