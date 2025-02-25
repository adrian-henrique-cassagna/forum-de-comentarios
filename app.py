from flask import Flask, redirect, render_template, request
import datetime

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/post/menssagem", methods=["POST"])
def cadastra_ms():

    usuario = request.form.get("nome")
    menssagem = request.form.get("comentario")
    data_hora = datetime.datetime.now()
    
    return redirect("/")

app.run(debug=True)