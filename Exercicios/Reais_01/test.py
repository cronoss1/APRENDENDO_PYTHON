"""
O erro está aqui: você chamou produtos.keys() — mas produtos é uma lista (list) de dicionários, não um dicionário. 
Listas não têm método keys(), por isso o Python levanta: AttributeError: 'list' object has no attribute 'keys'

O que isso significa (curto)

produtos tem o formato: [ {...}, {...}, {...} ] — é uma lista.
keys() é um método de dicionários (ex.: um_produto.keys() funciona, mas lista_de_produtos.keys() não).
Como corrigir (opções rápidas)

Se só quer inspecionar as chaves de um produto (ex.: primeiro item): produtos[0].keys()

Se quer ver as chaves de todos os produtos: for p in produtos: print(p.keys())

Se quer uma lista com os nomes dos produtos: nomes = [p['nome'] for p in produtos]

Para o exercício específico (dicas práticas):

Preço médio: avg = sum(p['preco'] for p in produtos) / len(produtos)
Produto mais caro / mais barato: mais_caro = max(produtos, key=lambda p: p['preco']) mais_barato = min(produtos, key=lambda p: p['preco'])
Filtrar eletrônicos e ordenar decrescente por preço: eletr = [p for p in produtos if p['categoria'] == "Eletrônicos"] eletr_ordenados = sorted(eletr, key=lambda p: p['preco'], reverse=True)
O que eu sugiro que você faça agora

Substitua chaves = produtos.keys() por uma das abordagens acima conforme o objetivo.
Se quiser, cole aqui o trecho corrigido e eu reviso — ou eu posso aplicar a correção no arquivo R_01.py se você quiser que eu faça a edição por você. Qual prefere?
"""


