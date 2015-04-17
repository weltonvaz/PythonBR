#/usr/bin/env python3
#coding: utf-8
import os
os.system('clear')

import json, mechanize
 
#recebe um jogador e retorna um dicionário com apenas as informações que queremos, podendo calcular informações interessantes.
def info(jogador):
    return {
        'nome': jogador['apelido'].encode('utf-8'),
        'time': jogador['clube']["nome"].encode('utf-8'),
        'pontos': float(jogador['pontos']),
        'chance_de_valorizar': "alta" if float(jogador['pontos'])<float(jogador['media']) else "baixa"
    }
 
# br será o objeto que simula o browser
br = mechanize.Browser()
 
# Abre a página de login Cartola através do mechanize
br.open('https://loginfree.globo.com/login/438')
 
#Na página, selecionamos o primeiro form presente. 'nr=0' indica que estamos selecionando o form de índice 0 dentre os encontrados.
#Analisando a página, vemos que realmente só há um form.
#Após selecionarmos o form, preenchemos os campos com username e senha que permitam fazer o login.
br.select_form(nr=0)
br.form['login-passaporte'] = 'SEU_EMAIL'
br.form['senha-passaporte'] = 'SUA_SENHA'
br.submit()
 
jogadores = []
 
for i in range(43):
    r = br.open("http://cartolafc.globo.com/mercado/filtrar.json?page="+str(i+1))
    j = json.loads(r.read())
    jogadores.extend(j['atleta'])
 
#ordem decrescente de pontos
results = sorted(map(info, jogadores), key=lambda k: -k['pontos'])
 
for j in results:
    s = "{nome}, do {time}, fez {pontos} pontos e tem chance {chance_de_valorizar} de valorizar".format(**j)
    print(s)
