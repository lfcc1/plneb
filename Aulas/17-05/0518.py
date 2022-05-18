import spacy
import re
import json

nlp = spacy.load('en_core_web_sm')

#file = open("book1.txt",'r',encoding='utf-8')
file1 = open("Book 1 - The Philosopher's Stone.txt",'r',encoding='utf-8')
text = file1.read()

def preprocesso(texto):
    texto = re.sub(r'Page \| \d+ Harry Potter and the Philosophers Stone - J\.K\. Rowling', '', texto)
    texto = re.sub(r'\n+', ' ', texto)
    return texto

doc = nlp(preprocesso(text))

pessoas = {}

for frase in doc.sents:

    for entity in frase.ents:
        if entity.label_ == "PERSON" or entity.label_ == 'ORG':

            if entity.text not in pessoas:
                pessoas[entity.text] = {}

            for entity1 in frase.ents:
                if entity1.label_ == "PERSON" or entity1.label_ == 'ORG':
                    
                    if entity.text != entity1.text:
                        if entity1.text in pessoas[entity.text]:
                            pessoas[entity.text][entity1.text] += 1
                        else:
                            pessoas[entity.text][entity1.text] = 1


print(pessoas)
filejson = open("filejson.json", 'w', encoding='utf-8')
json.dump(pessoas, filejson, indent = 4, ensure_ascii=False)

'''
# 1a parte

# Find named entities, phrases and concepts
pessoas = {}
for entity in doc.ents:
    if entity.label_ == 'PERSON' or entity.label_ == 'ORG':
        if entity.text not in pessoas:
            pessoas[entity.text] = 1
        else:
            pessoas[entity.text] = pessoas[entity.text] + 1
        #print(entity.text, entity.label_)

pessoas_sorted = sorted(pessoas.items(), key=lambda elemento:elemento[1],reverse=True)

for key, value in pessoas_sorted:
    print(key,value)
'''

