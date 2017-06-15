def matriz(m, n):
    matriz = []
    for i in range(1, m+1):
        linha = []
        for j in range(1, n+1):
            elem = input("Digite o %dx%d elemento: " %(i, j))
            linha.append(elem)
       
        matriz.append(linha)
 
    return matriz

print(matriz(2,3))
