#Lista de metodos uteis para usar com dicionários.
pessoa = {"nome": "Ana", "idade": 25}

# Acessar
print(pessoa.get("nome"))     # "Ana"
print(pessoa.keys())          # ['nome', 'idade'] (chaves)
print(pessoa.values())        # ['Ana', 25] (valores)

# Modificar
pessoa["cidade"] = "Rio"     # Adiciona nova chave
pessoa.update({"idade": 26}) # Atualiza valor

# Remover
idade = pessoa.pop("idade")   # Remove e retorna o valor