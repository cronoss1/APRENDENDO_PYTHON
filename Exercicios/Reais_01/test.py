"""
    Valida se um e-mail atende aos critérios:
    - Deve conter um '@'
    - Deve ter um domínio válido (.com, .com.br, .org, etc)
    - Não pode conter espaços
    - Deve ter pelo menos 3 caracteres antes do '@'
    Retorna True se válido, False caso contrário
    """

email = "usuario@email.br "
dominios_validos = [".com", ".br", ".org", ".com.br"]

if "@" in email:
    print("contem @")
if " " in email:
    print("contém espaços")
if not any(dominio in email for dominio in dominios_validos):
    print("domínio inválido")



print(len(email))