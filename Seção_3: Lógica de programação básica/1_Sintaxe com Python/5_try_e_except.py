"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""
numero = input(
    "Digite um número: "
)

try: # O try executa o código até que um erro aconteça, onde ele pula direto pro except.
    numero_float = float(numero)
    print(f"FLoat: {numero_float}")
except: # O except executa caso algum erro ocorra no try.
    print("Isso não é um número")