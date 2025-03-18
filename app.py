from flask import Flask, redirect, render_template, request
import datetime
from model.control_mensagem import Mensagem

app = Flask(__name__)

@app.route("/")
def home_page():
    mensagens = Mensagem.lista_mensagens()
    return render_template("index.html", mensagens = mensagens)

@app.route("/post/menssagem", methods=["POST"])
def cadastra_ms():
    usuario = request.form.get("nome")
    mensagem = request.form.get("comentario")

    Mensagem.cadastra_menssagem(usuario, mensagem)
    
    return redirect("/")

@app.route("/deleta_mensagem/<codigo>")
def deleta_mensagem(codigo):
    Mensagem.deleta_mensagem(codigo)
    return redirect("/")

@app.route("/curtidas/<curtidas>")
def curtidas_add(curtida):
    Mensagem.curtidas(curtida)
    return redirect("/")

if __name__ == __name__:
    app.run(debug=True)