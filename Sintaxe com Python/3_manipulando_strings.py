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
# a sengunda é utilizando o método (format) e a última é utilizando (f strings).

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

print("Olá, me chamdo %s. Eu tenho %d anos de idade, trabalho como %s e estou"
" matriculado no curso de %s." % (nome, idade, profissao, linguagem))

# 3. f-string:
# Exemplo:

nome = "Gustavo"
idade = 25
profissao = "programador"
linguagem = "Python"

print("Olá, me chamdo %s. Eu tenho %d anos de idade, trabalho como %s e estou"
" matriculado no curso de %s." % (nome, idade, profissao, linguagem))
