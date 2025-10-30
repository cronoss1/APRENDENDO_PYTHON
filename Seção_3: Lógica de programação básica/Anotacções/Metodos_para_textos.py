#Lista de metodos uteis para usar com string.
texto = " Python é Legal! "

# Transformação
print(texto.upper())        # " PYTHON É LEGAL! " (maiúsculas)
print(texto.lower())        # " python é legal! " (minúsculas)
print(texto.strip())        # "Python é Legal!" (remove espaços)
print(texto.title())        # " Python É Legal! " (primeiras maiúsculas)

# Busca e verificação
print(texto.find("é"))      # 8 (posição)
print("Python" in texto)    # True (verifica se contém)
print(texto.startswith(" ")) # True (começa com)
print(texto.endswith("! "))  # True (termina com)

# Substituição
print(texto.replace("Legal", "Incrível"))  # " Python é Incrível! "

# Divisão e junção
frases = "um,dois,três".split(",")     # ['um', 'dois', 'três']
juntado = "-".join(["a", "b", "c"])    # "a-b-c"