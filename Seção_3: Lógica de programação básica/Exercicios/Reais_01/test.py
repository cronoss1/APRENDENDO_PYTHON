nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

if nome != "" and idade != "":
    print(f"Seu nome é {nome}")
    print(f"Seu nome investido é {nome[::-1]}")
    if nome == " ":
        print("Seu nome contem espaços")
    else:
        print("Seu nome não contem espaços")
    print(f"Seu nome contem {len(nome)} letras")
    print(f"A primeira letra do seu nome é {nome[0]}")
    print(f"A ultima letra do seu nome é {nome[-1]}")
else:
    print("Desculpe, você deixou campos vazios")