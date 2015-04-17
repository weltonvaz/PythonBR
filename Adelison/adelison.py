#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
os.system('clear')

ids = open('ids.txt')
with open("exemplobase.txt", "r") as arq:
    for linha in arq:
        for x in ids:
            if x:
                print (linha)
                break
            continue