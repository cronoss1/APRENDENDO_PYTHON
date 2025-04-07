# MANIPULAÇÃO DE DATAS E HORAS

"""
O que é o módulo datetime?:
O módulo 'datetime' em Python é usado para lidar com datas e horas. 
Ele possui várias classes úteis como date, time e timedelta.
"""
# Exemplo:
# from datetime import date -> Segunda forma de importa.
import datetime # Importando

data = datetime.date(2023, 8, 25) # Utilizando a classe date(data).
print(data) # 2023-08-25

"""
Introdução Manipulação de datas e horas:
Podemos criar e manipular objetos date, time e datetime de várias maneiras. 
Por exemplo, podemos adicionar e subtrair datas, verificar a diferença entre datas e muito mais.
"""
# Exemplo:
import datetime

# Criando data e hora
data_hora = datetime.datetime(2025, 9, 27, 14, 34)
print(data_hora) # 2025-09-27 14:34:00

# Adcionando uma semana
data_hora = data_hora + datetime.timedelta(weeks=1) 
print(data_hora) # 2025-10-04 14:34:00

"""
Introdução Conversão e formatação de datas e horas:
Python também permite converter e formatar datas e horas. 
Para isso, usamos os métodos 'strftime' (string format time) e 'strptime' (string parse time).
"""
# Exemplo_1:
import datetime

d = datetime.datetime.now() # data e hora atual 

# Formatando date e hora
print(d.strftime("%d/%m/%Y %M:%M")) # Formatação

# Convertendo string para datetime
date_string = "20/08/2024 13:45" # Variável com a str que precisa ser convertida
d = datetime.datetime.strptime(date_string, "%d/%m/%Y %H:%M") # Formatação
print(d) # Retorna a data e hora formatada

# Exemplo_2:
from datetime import datetime # Importando datetime

data_hora_atual = datetime.now() # Variável com data e hora atual
data_hora_str = "2023-10-20 10:20" # Variável com a str que precisa ser convertida
mascara_ptbr = "%d/%m/%Y %a" # Variável com formatação em ptbr
mascara_en = "%Y-%m-%d %H:%M" # Variável com formatação em en

print(data_hora_atual.strftime(mascara_ptbr)) # Retorna a data e hora atual com a formatação ptbr
# Variável       modulo  str para time  vai ser convertida   formatação
#    |             |          |          |                     |
#    V             V          V          V               V<-----
data_convertida = datetime.strptime(data_hora_str, mascara_en) # Formantado a data e hora para en
print(data_convertida) # Retorna a data e hora convertida em en
print(type(data_convertida)) # Retorna o tipo da variável data_convertida

"""
Introdução Trabalhando com timezones:
Quando trabalhamos com data e hora, lidar com fusos horários é uma necessidade comum. 
Python facilita isso através do módulo 'pytz'.
"""
# Exemplo:
import datetime
import pytz

# Criando datetime com timezone
d = datetime.datetime.now(pytz.timezone("America/Sao_Paulo"))
print(d) # Ira retornar a data e hora atual na timezone de São Paulo.

"""
Trabalhando com tz sem bibliotecas externas:
O Python permite fazer isso com o módulo datetime padrão, embora seja um pouco mais 
complexo do que usando bibliotecas como 'pytz'.
"""
# Exemplo:
import datetime

# Criando datetime com timezone
d = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-3), "BRT"))
print(d) # Ira retornar a data e hora atual menos 3 horas.

# Convertendo para outro timezone
d_utc = d.astimezone(datetime.timezone.utc)
print(d_utc)

