import os

lista = os.listdir("/home/usuarioqualquer/diretorioqualquer")

for nome in lista:
    novo_nome = nome.replace("(", "-")
    os.rename(nome, novo_nome)
