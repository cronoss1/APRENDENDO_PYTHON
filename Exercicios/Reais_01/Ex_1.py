# Problema 1: Validador de E-mails

def validar_email(email):
    """
    Valida se um e-mail atende aos critérios:
    - Deve conter um '@'
    - Deve ter um domínio válido (.com, .com.br, .org, etc)
    - Não pode conter espaços
    - Deve ter pelo menos 3 caracteres antes do '@'
    Retorna True se válido, False caso contrário
    """
    # Sua solução aqui
    
    pass

# Teste suas soluções:
print(validar_email("usuario@email.com"))     # True
print(validar_email("user@dominio.com.br"))   # True  
print(validar_email("ab@x.com"))              # False (muito curto)
print(validar_email("semarroba.com"))         # False