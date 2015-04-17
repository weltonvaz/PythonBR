cont = 0
lista = []
for x in range(1,26):
    for y in range(1,26):
        if y == x:
            continue
        for z in range(1,26):
            if z == x or z ==y:
                continue
            cont += 1
            lista.append([(x),(y),(z)])

clones = 0

for duplos in range(0,(len(lista))):
    for clone in range(0,(len(lista))):
        if lista[duplos] == lista[clone]:
            lista.remove(clone)
print(len(lista))

for v in range(1,1000):

