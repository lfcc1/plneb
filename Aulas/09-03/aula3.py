#!/usr/bin/env python3

import re

ficheiro = open('dicionario_medico.txt','r',encoding = 'utf_8')
ficheiro1=open('dicionario_medico.html','w',encoding = 'utf_8')

texto = ficheiro.read()
texto = re.sub(r'\f',r'=',texto)
texto = re.sub(r'\n\n(.+)',r'\n\n@\1',texto)
texto = re.sub(r'(@.+\n)',r'\1#',texto)

def procsig(m):
    conteudo = m[0]
    conteudo=re.sub(r'#','',conteudo)
    texto=''
    definicao=''
    sinonimos=re.split(r';', conteudo)
    for a in sinonimos:	
        a.strip() #tira espaços do inicio e fim
        if len(a)<15:
                texto+="<li>"+a+"</li>"
        else:
            definicao+=a+" "
    return(f'''<ul>
    {texto}
    </ul>
        <blockquote>{definicao}</blockquote>''')

texto = re.sub(r'#[^@]+', procsig, texto) #Tudo exceto o caractere @


print('''
<html>
    <head>
        <meta charset="UTF-8"/>
    </head>
<body>
    <h1>Processamento de Linguagem Natural</h1>
    <h2>Fantástico Dicionário Médico </h2>''', file=ficheiro1)

print(texto,file=ficheiro1)

print('''
</body>
</html>''', file=ficheiro1)