import urllib.request
from datetime import date
import time

dolar_atual = 0
dolar_armazenado = 0

#data_usuario = float(input('Digite uma data: '))
data_usuario = '2014-11-24'
hj =  date.today()
print('A data que o usuário escolheu é %s' % data_usuario)
print('A data de hoje é %s' % hj)

if data_usuario == hj:
    data_usuario = float(input('Digite uma outra data pois a digitada é a atual: '))    
else:
    while hj != data_usuario:
        pagina = urllib.request.urlopen('http://www.valor.com.br/valor-data')
        texto = pagina.read().decode('utf8')
        onde = texto.find('DÓLAR COM.')
        inicio = onde + 45
        fim = inicio + 6
        dolar_atual = str(texto[inicio:fim])
        print('Cotação Dólar atual: %s' % dolar_atual)
        with open('log.txt', 'a') as arquivo:
            if dolar_atual != dolar_armazenado:
                arquivo.write('O valor do Dólar esta: %s - Start: %s\n' %(dolar_atual, time.ctime()))
                print('O valor do Dólar esta: %s - Start: %s ' %(dolar_atual, time.ctime()))
                print('Gravado com sucesso...')
                dolar_armazenado = dolar_atual
                time.sleep(5)
            else:
                print('O valor do Dólar esta: %s - Start: %s ' %(dolar_atual, time.ctime()))
                print('Não Gravado...')
                dolar_armazenado = dolar_atual
                time.sleep(5)
