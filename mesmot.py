from itertools import groupby

g = (["oi", "pato", "prato", "macaco", "po", "jantar"])
mesmo_tamanho = lambda data: [list(g) for k, g in groupby(sorted(data, key=lambda x:len(x)), key=lambda x:len(x))]

print(mesmo_tamanho)
