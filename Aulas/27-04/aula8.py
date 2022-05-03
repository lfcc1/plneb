import requests 
from bs4 import BeautifulSoup 

html_doc = requests.get("https://www.atlasdasaude.pt/doencasaaz/a")

soup = BeautifulSoup(html_doc.text, 'html.parser')

for div_pai in soup.find_all("div", class_="views-row"):
    print("##",div_pai.findChildren(recursive=False)[0])
    break;

print(len(soup.find_all("div",class_="field-content")))





