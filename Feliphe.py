x = 1
maior_valor = 0
menor_valor = 0
valor_atual = 0
while (x < 5):
    valor_atual = int(input("Digite o %i valor: " %x))
    if x == 1:
        maior_valor = valor_atual
        menor_valor = valor_atual

    if valor_atual > maior_valor:
        maior_valor = valor_atual
    elif valor_atual < menor_valor:
        menor_valor = valor_atual
    x += 1

print("O maior valor e %i e o menor e %i" %(maior_valor, menor_valor))