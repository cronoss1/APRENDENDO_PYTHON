#Problema 2: Processador de Texto
from collections import Counter
def analisar_texto(texto):
    """
    Analisa um texto e retorna um dicionário com:
    - numero_palavras: total de palavras
    - palavra_mais_frequente: a palavra que mais aparece
    - media_comprimento: comprimento médio das palavras
    """
    # Sua solução aqui
    numero_palavras = texto.split() # Divide o texto em palavras individuais
    contador = Counter(numero_palavras) # Conta a quantidade de palavras 
    palavra_mais_frequente = contador.most_common(1)[0][0] # Mostra a palavra mais frequênte
    soma_comprimento = sum(len(palavra) for palavra in numero_palavras) # Faz a soma do comprimento de cada palavra
    media_comprimento = soma_comprimento / len(numero_palavras) # Divide o comprimento total pelo número de palavras
    print(len(numero_palavras))
    print(palavra_mais_frequente)
    print(media_comprimento)
    pass

texto_exemplo = "python é uma linguagem poderosa python é fácil de aprender"
print(analisar_texto(texto_exemplo))