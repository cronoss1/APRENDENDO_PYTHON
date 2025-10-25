"""
    Valida se um e-mail atende aos critérios:
    - Deve conter um '@'
    - Deve ter um domínio válido (.com, .com.br, .org, etc)
    - Não pode conter espaços
    - Deve ter pelo menos 3 caracteres antes do '@'
    Retorna True se válido, False caso contrário
    """

email = "usa@email.br "
dominios_validos = [".com", ".br", ".org", ".com.br"]

if "@" in email: # Verifica se tem arroba
    print("contem @")
if " " in email: # Verifica se tem espaços
    print("contém espaços")
if not any(dominio in email for dominio in dominios_validos): # Verifica domínio válido
    print("domínio inválido")
if email.find("@") >= 3: # Verifica tamanho antes do '@'
    print("Bom tamanho antes do @")
else:
    print("Não tem pelo menos 3 caracteres antes do '@'")
print(len(email))