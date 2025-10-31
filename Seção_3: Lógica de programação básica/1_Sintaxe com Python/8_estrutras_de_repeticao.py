"""
# Estruturas de Repetição
# São estruturas utilizadas para repetir um trecho de código um determinado número de vezes.
# Esse número pode ser conhecido previamente ou determinado através de uma expressão lógica.
"""
# Exemplo (while): Executa uma ação enquanto uma condição for verdadeira
contador = 0

while contador <= 10: # Condição 
     print(contador)
     contador = contador + 1

print('Acabou')

# Exemplo (break): Instrução usada para interromper a execução de um loop (como for ou while).
contador = 0
while contador < 10:
    if contador == 6:
        break
    print(contador)
    contador += 1



"""
# Exemplo (for): E usado quando sabemos o número exato de vezes que nosso bloco de código
# deve ser executado.
texto = input("Informe um texto:") # Variavel
VOGAIS = "AEIOU" # Laço de repetição

for letra in texto:
    # Transformando letra para maiusculo.
    if letra.upper() in VOGAIS:
        print(letra, end="") # adiciona uma quebra de linha
print()

# Exemplo (for/else): else executa depois do laço de repetição
texto = input("Informe um texto:") # Variavel
VOGAIS = "AEIOU" # Laço de repetição

for letra in texto:
    # Transformando letra para maiusculo.
    if letra.upper() in VOGAIS:
        print(letra, end="") # adiciona uma quebra de linha
else:
    print("Executado depois do laço")

# Exemplo (range): Usado para produzir uma sequência de números.
# Ex_1: 
for numero_1 in range(0, 11): # Tipo range(início, fim)
    print(numero_1, end="")
# Ex_2:
for numero_2 in range(0, 51, 5):   
    print(numero_2, end="") # Tipo range(início, fim, passo) a diferença entre cada número na sequência.
"""