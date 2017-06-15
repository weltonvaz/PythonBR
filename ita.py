lista = []
for x in range(1,8):
    for y in range(1,8):
        for z in range(1,8):
            lista.append(str(x)+str(y)+str(z))
# print (len(lista))

# for a in lista:
#    if (a[0] == a[1]) or (a[1] == a[2]) or (a[1] == a[2]):
#        lista.remove(a)
# print (len(lista))

for b in lista:
    if b[0] == "34567" and b[1]+b[2] == "77":
        print (b)

# print (lista)
# print (len(lista))