import requests 
from bs4 import BeautifulSoup 
import string

def normaliza(string):
    string=string.replace("\xa0"," ")
    return string.strip()

def getdescription(url):
    html_doc = requests.get("https://www.atlasdasaude.pt"+url)

    soup = BeautifulSoup(html_doc.text, 'html.parser')
    return soup.find_all("div", class_="field-items")[1]

dic={}


#for i in list(string.ascii_lowercase)
for i in list("a"):
    html_doc = requests.get("https://www.atlasdasaude.pt/doencasaaz/"+i)

    soup = BeautifulSoup(html_doc.text, 'html.parser')


    for div_pai in soup.find_all("div", class_="views-row"):
        termo=div_pai.findChildren(recursive=False)[0].h3.a.text
        url=div_pai.findChildren(recursive=False)[0].h3.a["href"]
        descricao=getdescription(url)
        definicao=div_pai.findChildren(recursive=False)[1].div.text
        
        dic[normaliza(termo)]={ "definição": normaliza(definicao), "descrição": descricao }
        
print(dic)
    #break;
print(len(dic))

#print(len(soup.find_all("div",class_="field-content")))
