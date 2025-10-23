#Problema 4: Processamento de Dados de Usuários

def processar_usuarios(usuarios):
    """
    Processa uma lista de usuários e retorna:
    - usuarios_ativos: lista apenas com usuários ativos
    - media_idade: média de idade dos usuários ativos
    - usuarios_por_cidade: dicionário agrupando por cidade
    - usuario_mais_velho: nome do usuário mais velho
    """
    pass

usuarios = [
    {"id": 1, "nome": "Ana", "idade": 25, "cidade": "São Paulo", "ativo": True},
    {"id": 2, "nome": "João", "idade": 30, "cidade": "Rio de Janeiro", "ativo": False},
    {"id": 3, "nome": "Maria", "idade": 28, "cidade": "São Paulo", "ativo": True},
    {"id": 4, "nome": "Pedro", "idade": 35, "cidade": "Belo Horizonte", "ativo": True}
]

resultado = processar_usuarios(usuarios)
print(resultado)