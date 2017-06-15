# !/usr/bin/python
#coding: utf-8

import os, sys, time
os.system('clear')

# listagem de diretorios
print "Os diretorios são: %s"%os.listdir(os.getcwd())

# renomea diretorio ''pasta1"
os.rename("pasta1","diretorio")

print "Successo Diretório renomeado."
time.sleep (15)
os.system('clear')

# listing directories after renaming "tutorialsdir"
print "Os diretorios agora: %s" %os.listdir(os.getcwd())\
