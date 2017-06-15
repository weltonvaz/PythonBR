# !/usr/bin/python
#coding: utf-8

import os

lista = os.listdir("/home/welton/workspace/Pythonbr/Hugo/media/")

for nome in lista:
    novo_nome = nome.replace("dir", "-")
    os.rename(nome, novo_nome)
