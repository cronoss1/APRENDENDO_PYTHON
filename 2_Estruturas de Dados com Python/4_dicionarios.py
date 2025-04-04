# CRIAÇÃO E ACESSO AOS DADOS

"""
Criando dicionários:
Um dicionário é um conjunto não-ordenado de pares chave:valor, onde as chaves são 
únicas em uma dada instância do dicionário. Dicionários são delimitados por chaves: {}, 
e contém uma lista de pares chave:valor separada por vírgulas.
"""
# Exemplo:
pessoa = {"nome": "Guilherme", "idade": 28}

pessoa = dict(nome="Guilherme", idade=28)

pessoa["telefone"] = "3333-1234"  # {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}

"""
Acesso aos dados:
Os dados são acessados e modificados através da chave.
"""
# Exemplo:
dados = {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}

dados["nome"]  # "Guilherme"
dados["idade"]  # 28
dados["telefone"]  # "3333-1234"

dados["nome"] = "Maria"
dados["idade"] = 18
dados["telefone"] = "9988-1781"

dados  # {"nome": "Maria", "idade": 18, "telefone": "9988-1781"}

"""
Dicionários aninhados:
Dicionários podem armazenar qualquer tipo de objeto Python como valor, desde que a chave 
para esse valor seja um objeto imutável como (strings e números).
"""
# Exemplo:
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

contatos["giovanna@gmail.com"]["telefone"]  # "3443-2121"

"""
Iterar dicionários:
A forma mais comum para percorrer os dados de um dicionário é utilizando o comando for.
"""
# Exemplo:
for chave in contatos:
    print(chave, contatos[chave])

for chave, valor in contatos.items():
	print(chave, valor)

# guilherme@gmail.com {'nome': 'Guilherme', 'telefone': '3333-2221'}
# giovanna@gmail.com {'nome': 'Giovanna', 'telefone': '3443-2121'}
# chappie@gmail.com {'nome': 'Chappie', 'telefone': '3344-9871'}
# melaine@gmail.com {'nome': 'Melaine', 'telefone': '3333-7766'}

# MÉTODOS DA CLASSE DICT

# {}.clear: Usado para apagar todos os valores do dicionário.
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

contatos.clear()
contatos  # {}

# {}.copy: Usado para criar uma copia do dicionário
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
}

copia = contatos.copy()
copia["guilherme@gmail.com"] = {"nome": "Gui"}

contatos["guilherme@gmail.com"]  # {"nome": "Guilherme", "telefone": "3333-2221"}
copia["guilherme@gmail.com"]  # {"nome": "Gui"}

# {}.fromkeys: Usado para criar chaves no dicionário, com valor ou não.
dict.fromkeys(["nome", "telefone"])  # {"nome": None, "telefone": None}

dict.fromkeys(["nome", "telefone"], "vazio")  # {"nome": "vazio", "telefone": "vazio"}

# {}.get: Segunda forma de acessar valores de um dicionário.
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
}

contatos["chave"]  # KeyError

contatos.get("chave")  # None
contatos.get("chave", {})  # {}
contatos.get("guilherme@gmail.com", {})  # {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}

# {}.items: Usado para retornar uma lista de tuplas.
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme","telefone": "3333-2221"}
}

contatos.items()  # dict_items([('guilherme@gmail.com', {'nome': 'Guilherme', 'telefone': '3333-2221'})])

# {}.keys: Usado para retornar somente as chaves do nosso dicionário.
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme","telefone": "3333-2221"}
}

contatos.keys()  # dict_keys(['guilherme@gmail.com'])

# {}.pop: Usado para remover uma chave do seu dicionário.
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme","telefone": "3333-2221"}
}

contatos.pop("guilherme@gmail.com")  # {'nome': 'Guilherme', 'telefone': '3333-2221'}
contatos.pop("guilherme@gmail.com", {})  # {}

# {}.popitem: Usado para remover elementos do seu dicionário na sequência.
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme","telefone": "3333-2221"}
}

contatos.popitem()  # ('guilherme@gmail.com', {'nome': 'Guilherme', 'telefone': '3333-2221'})
contatos.popitem()  # KeyError

# {}.setdefault: Usado para adicionar uma chave e o valor ao dicionário, mas se o mesmos já existirem
# ele retorna o valor existente.
contato = {'nome': 'Guilherme', 'telefone': '3333-2221'}

contato.setdefault("nome", "Giovanna")  # "Guilherme"
contato  # {'nome': 'Guilherme', 'telefone': '3333-2221'}

contato.setdefault("idade", 28)  # 28
contato  # {'nome': 'Guilherme', 'telefone': '3333-2221', 'idade': 28}

# {}.update: Usado para atulizar nosso dicionário.
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme","telefone": "3333-2221"}
}

contatos.update({"guilherme@gmail.com": {"nome": "Gui"}})
contatos  # {'guilherme@gmail.com': {'nome': 'Gui'}}

contatos.update({"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3322-8181"}})
contatos  # {'guilherme@gmail.com': {'nome': 'Gui'}, 'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3322-8181'}}

# {}.values: Usado para retornar todos os valores do nosso dicionário.
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

contatos.values()  # dict_values([{'nome': 'Guilherme', 'telefone': '3333-2221'}, {'nome': 'Giovanna', 'telefone': '3443-2121'}, {'nome': 'Chappie', 'telefone': '3344-9871'}, {'nome': 'Melaine', 'telefone': '3333-7766'}])

# in: Usado para saber se a chave existe no dicionário.
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

"guilherme@gmail.com" in contatos  # True
"megui@gmail.com" in contatos  # False
"idade" in contatos["guilherme@gmail.com"]  # False
"telefone" in contatos["giovanna@gmail.com"]  # True

# del: Usado para remover valores ou toda a chave do dicionário.
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

del contatos["guilherme@gmail.com"]["telefone"]
del contatos["chappie@gmail.com"] 

contatos # {'guilherme@gmail.com': {'nome': 'Guilherme'}, 'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3443-2121'}, 'melaine@gmail.com': {'nome': 'Melaine', 'telefone': '3333-7766'}}

