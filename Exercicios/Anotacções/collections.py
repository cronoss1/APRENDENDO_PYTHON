"""
collections é um módulo padrão do Python que reúne estruturas de dados úteis além das built-ins (list, dict, etc.). 
Exemplos nele: deque, defaultdict, namedtuple, OrderedDict (embora hoje dict já preserve ordem), e Counter.
"""
from collections import Counter
"""
Counter é uma subclasse de dict especializada para contagem de elementos. Dado um iterável (como uma lista de palavras), 
Counter retorna quantas vezes cada elemento aparece.
"""
palavras = ["python", "é", "uma", "python", "fácil"]
contagem = Counter(palavras)
# contagem -> Counter({'python': 2, 'é': 1, 'uma': 1, 'fácil': 1})
"""
Métodos úteis do Counter

most_common(n) → retorna uma lista dos n elementos mais comuns como [(elem, count), ...], em ordem decrescente de frequência. most_common(1) pega o top-1.

elements() → itera pelos elementos repetidos conforme sua contagem (útil em algumas situações).

update(iterable_or_mapping) → incrementa contagens a partir de outro iterável ou dicionário.

subtract(...) → subtrai contagens.

clear() e copy() → como em dicionários normais.

Você também pode usá-lo como um dicionário: contagem['python'] devolve a contagem (0 se não existir).
"""