#!/usr/bin/env python3

import re
import json 

# biblioteca das traduções
# from deep_translator import GoogleTranslator



#Abrir ficheiro html
livro_doencas = open('livro_doencas.html','w')

#Abrir dicionario
dicionario = open('jsonfile.json','r',encoding = 'utf_8')
dicionario = json.load(dicionario)

#Dicionário com os termos em minusculo
dicionario_minusculo={x.lower():dicionario[x] for x in dicionario}

#Abrir livro de doenças e ler
doencas = open('lixo','r', encoding='utf_8')
doencas = doencas.read()

#Abrir dicionario de traducoes
traducoes=open('termos_traduzidos.txt','r',encoding='utf_8')

#Adicionar ao dicionário atual um novo indice ('en')
#ESTA A DAR ERRO em l+, Palvra e Significado pois foram apagados do original!
#bastou remover estes 3 termos do ficheiro termos traduzidos

for linha in traducoes:
	v1,v2=linha.split('@')
	dicionario_minusculo[v1.strip().lower()]['en']=v2.strip() #colocar novo indice de traducao
	
print(dicionario_minusculo) #teste de verificação

#Termos do dicionário e remoção de "outliers"
chaves=dicionario_minusculo.keys()

lista_exclusoes=["e","de","para","l+","en"]
chaves=[re.escape(x) for x in chaves if x not in lista_exclusoes]

#Separação das chaves com | em vez de ,
chaves=r"\b("+"|".join(chaves)+r")\b"

#Função que retorna o significado do termo
def processa_termo(termo):
	termo_original=termo[0]
	
	termo=termo[0].lower()
	
	definicao=dicionario_minusculo[termo]["desc"]
	
	termo_traduzido=dicionario_minusculo.get(termo)
	
	termo_traduzido=termo_traduzido.get("en")
	
	termo=f"<a href=# title='Tradução: {termo_traduzido}&#10;Definição: {definicao}'>"+termo_original+"</a>"
	return termo

#Expressão regular (selecao dos termos)
doencas=re.sub(chaves, processa_termo, doencas, flags=re.I)

#Expressão regular (substituir new line por break)
doencas=re.sub(r'\n',r'<br>',doencas)

#Expressão regular (substituir os \f por linha)
doencas=re.sub(r'\f',r'<hr>',doencas)


#Criação do documento html

print('''
<html>
    <head>
        <meta charset="UTF-8"/>
    </head>
<body>
    <h1>Processamento de Linguagem Natural</h1>
    ''' + doencas, file=livro_doencas)

print('''
</body>
</html>''', file=livro_doencas)







