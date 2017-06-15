n1 = float(input('Ciência Humanas: '))
p1 = int(input('Peso: '))
n2 = float(input('Ciências da Natureza: '))
p2 = int(input('Peso: '))
n3 = float(input('Linguagens: '))
p3 = int(input('Peso: '))
n4 = float(input('Matemática: '))
p4 = int(input('Peso: '))
n5 = float(input('Redação: '))
p5 = int(input('Peso: '))

calculo_media = ((n1*p1)+(n2*p2)+(n3*p3)+(n4*p4)+(n5*p5))/(p1+p2+p3+p4+p5)

print('Sua média final é ', calculo_media)