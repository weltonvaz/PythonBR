import os
if os.name == "nt":
	os.system("cls")
else:
	os.system("clear")

def soma(*args):
    result = 0
    for elem in args:
        result += elem
    return result

print (soma(1, 2, 3, 4, 5))


