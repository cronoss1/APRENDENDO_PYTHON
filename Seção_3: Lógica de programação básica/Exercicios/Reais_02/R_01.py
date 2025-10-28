#mostre o preço médio dos produtos;
#Mostre o produto mais caro e o mais barato;
#Crie uma nova lista apenas com os produtos da categoria "Eletrônicos", ordenados por preço decrescente.

produtos = [
    {"nome": "Celular", "preco": 1500, "categoria": "Eletrônicos"},
    {"nome": "Camisa", "preco": 100, "categoria": "Vestuário"},
    {"nome": "Notebook", "preco": 3500, "categoria": "Eletrônicos"},
    {"nome": "Tênis", "preco": 250, "categoria": "Vestuário"},
    {"nome": "Fone de Ouvido", "preco": 200, "categoria": "Eletrônicos"}
]
"""
preco = [p[("nome", "preco")] for p in produtos]
media = sum(preco) / len(produtos)
caro = max(preco)
barato = min(preco)
  
print(media)
print(caro)
print(barato)
"""
mais_caro = max(produtos, key=lambda p: p["preco"])
mais_barato = min(produtos, key=lambda p: p["preco"])
eletro = [p for p in produtos if p["categoria"] == "Eletrônicos"]
eletro_ordena = sorted(eletro, key=lambda p: p["preco"], reverse=True)
print(mais_caro)
print(mais_barato)
print(eletro)

