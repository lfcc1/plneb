#!/usr/bin/env python3

import re

ficheiro = open('dicionario_medico.xml','r',encoding = 'utf_8')

texto = ficheiro.read()

texto = re.sub(r'<text.+?>',r'',texto) #remove a parte inicial

texto = re.sub(r'</text>',r'',texto) 

texto = re.sub(r'</page>',r'',texto)

texto = re.sub(r'<page.+>',r'',texto)

texto = re.sub(r'\n',r' ',texto)


#print(texto)

#termos_dic={} 

termos=[]

for termo,definicao in re.findall(r'<b>(.+?)</b>([^<]+)',texto):
    termos.append((termo.strip(),definicao.strip()))
    #termos_dic[termo.strip()]=definicao.strip()

print(dict(termos)) #transforma lista de tuplos em dicionario
#print(termos_dic)
#print(len(termos))

