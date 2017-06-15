#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
os.system('clear')

def regra_numeros(num1,num2):

	if (num1[-len(num2):]) == num2:
		return ("Os numeros %s e %s ==> encaixa" %(num1,num2))
	else:
		return ("Os numeros %s e %s ==> NÃO encaixa" %(num1,num2))

num1 = input("Digite um numero: ")
num2 = input("Digite um numero: ")

print (regra_numeros(num1,num2))