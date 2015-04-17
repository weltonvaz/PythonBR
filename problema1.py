#!/usr/bin/python

import os
os.system('clear')

def flights(arrivals):
    return (sorted(voo,key=lambda voo: ' ' if voo[1] == ' not_used' else voo[1]))

voo = [('B1', ' 13:45'), ('B2', ' 13:35'),('B3', ' 13:25'), ('B3', ' not_used'), ('B4', ' not_used')]

print (flights(voo))