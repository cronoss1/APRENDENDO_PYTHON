from collections import Counter
"""
    Analisa um texto e retorna um dicionário com:
    - numero_palavras: total de palavras 
    - palavra_mais_frequente: a palavra que mais aparece
    - media_comprimento: comprimento médio das palavras
"""
texto_exemplo = "python é uma linguagem poderosa python é fácil de aprender"
palavras = texto_exemplo.split() # Divide o texto em palavras
contador = Counter(palavras) # Conta a frequência de cada palavra
palavra_mais_frequente = contador.most_common(1)[0][0] # Palavra mais frequente
soma_comprimentos = sum(len(palavra) for palavra in palavras) # Soma dos comprimentos
media_comprimento = soma_comprimentos / len(palavras) # Comprimento médio

print(len(palavras)) # Contador de palavras
print(palavra_mais_frequente) # Palavra mais frequente
print(soma_comprimentos)
print(media_comprimento) # Comprimento médio
print(len(texto_exemplo))