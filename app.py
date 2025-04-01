from flask import Flask, redirect, render_template, request
import datetime
from model.control_mensagem import Mensagem
from model.control_user import Usuario

app = Flask(__name__)

@app.route("/")
@app.route("/cadastra/usuario")
def home_page():
    mensagens = Mensagem.lista_mensagens()
    return render_template("cadastro.html", mensagens = mensagens)

@app.route("/post/mensagem", methods=["POST"])
def cadastra_ms():
    usuario = request.form.get("nome")
    mensagem = request.form.get("comentario")
    Mensagem.cadastra_menssagem(usuario, mensagem)
    return redirect("/mensagem")

@app.route("/deleta_mensagem/<codigo>")
def deleta_mensagem(codigo):
    Mensagem.deleta_mensagem(codigo)
    return redirect("/mensagem")

@app.route("/curtidas/<curtida>")
def curtidas_add(curtida):
    Mensagem.curtidas(curtida)
    return redirect("/mensagem")

@app.route("/del-curtidas/<curtidas>")
def curtidas_del(curtidas):
    Mensagem.del_curtidas(curtidas)
    return redirect("/mensagem")

@app.route("/login")
def pag_login():
    return render_template("login.html")

@app.route("/cadastra/usuario", methods=["POST"])
def cadastra_usuario():
    
    login = request.form.get("login")
    usuario = request.form.get("usuario")
    senha = request.form.get("senha")

    Usuario.cadastro_usuario(login, usuario, senha)
    return redirect("/login")

if __name__ == __name__:
    app.run(debug=True)