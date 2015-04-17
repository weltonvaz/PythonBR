with open('arquivo.txt') as arq:
    status_texts = []
    for linha in arq:
        t = eval(linha)
        for status in t['text'].splitlines():
            status_texts.append(status)
...
print(status_texts)
