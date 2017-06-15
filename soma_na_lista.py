def soma_na_lista(n, lista):
    return n in [x + y for x in lista for y in lista if x != y]

print(soma_na_lista(5, [1, 2, 3, 4])) #-> True
print(soma_na_lista(9, [1, 2, 3, 4])) #-> False
print(soma_na_lista(0, [1, 2, 3, 4])) #-> False
print(soma_na_lista(8, [1, 2, 3, 4])) #-> False
print(soma_na_lista(4, [2, 2, 2, 2])) #-> False
print(soma_na_lista(4, [2, 2, 1, 3])) #-> True