
from flask import Flask, render_template
import json
app = Flask(__name__)

dbFile = open("jsonfile.json")
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

@app.route("/termos/<termo>")
def termo(termo):
    significado = {"designacao":termo,"desc":db[termo]["desc"]}
    return render_template("termo_view.html",termo = significado)



app.run(port=4000, debug=True)