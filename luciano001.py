import os
os.system("clear")

from Crypto.Cipher import Blowfish

name = 'luciano'
name += '.' * (8 - len(name) % 8)

cipher = Blowfish.new('python')
output = cipher.encrypt(name)

print(output)
