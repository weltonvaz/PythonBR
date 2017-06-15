from itertools import chain, zip_longest
s1 = '1357'
s2 = '246890'
print (''.join(''.join(x) for x in zip_longest(s1, s2, fillvalue='')))
print (''.join(chain.from_iterable(zip_longest(s1, s2, fillvalue=''))))
#a primeira solução é original do Hélio Meira, do grupo do Facebook Python Programadores
#a segunda solução é do Tonny via Telegram https://t.me/pythonbr
