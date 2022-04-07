
from flask import Flask, render_template, request
import re
import json
app = Flask(__name__)

dbFile = open("new_dict.json")
db = json.load(dbFile)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p> ola"

@app.route("/home")
def home():
    return render_template("home.html")



@app.route("/termos")
def termos():
    return render_template("termos_view.html",termos = db)


@app.route("/tabela")
def termos_tabela():
    return render_template("table_view.html",termos = db)

@app.route("/termos", methods=['POST'])
def termos_post():
    desc = request.form.get("desc")
    termo = request.form.get("termo")
    en = request.form.get("en")
    
    db[termo]={"desc":desc,"en":en}
    file = open("new_dict.json","w")
    json.dump(db,file,indent=4,ensure_ascii=False)
    return render_template("termos_view.html",termos = db)

@app.route("/termos/<termo>")
def termo(termo):
    significado = {"designacao":termo,"desc":db[termo]["desc"],"en":db[termo]["en"]}
    return render_template("termo_view.html",termo = significado)


@app.route("/termos/pesquisa")
def termos_pesquisa():
    palavra = request.args.get("palavra")
    lista = []
    if(palavra):
        for key, value in db.items():
            if(re.search(palavra,key) or re.search(palavra,value["desc"])):
                lista.append({"termo":key, "desc":value["desc"]})    
    return render_template("termos_pesquisa_view.html",termos = lista, palavra = palavra)

app.run(port=4000, debug=True)