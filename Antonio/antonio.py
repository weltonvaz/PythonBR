import os

if os.name == "nt":
    os.system("cls")
else:
    os.system("clear")

import math

limite = 1000

c = 1
p = 1
primos = [2,]
for numero in range(3,limite+1):
    ehprimo = 1
    for i in primos:
        if numero % i == 0:
            ehprimo = 0
            break
        if i > math.sqrt(numero):
            break
        c += 1
    if (ehprimo):
        primos.append(numero)
        print (numero,)
        p += 1

print ("Foram encontrados %d números primos." %p)
print ("Foram necessárias %d comparações." %c)