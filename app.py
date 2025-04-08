from flask import Flask, redirect, render_template, request, session
import datetime
from model.control_mensagem import Mensagem
from model.control_user import Usuario

app = Flask(__name__)

@app.route("/")
@app.route("/cadastra/usuario")
def home_page():

    return render_template("cadastro.html")


@app.route("/post/mensagem", methods=["POST"])
def cadastra_ms():

    usuario = request.form.get("nome")
    mensagem = request.form.get("comentario")

    Mensagem.cadastra_menssagem(usuario, mensagem)
    return redirect("/comentario")


@app.route("/deleta_mensagem/<codigo>")
def deleta_mensagem(codigo):

    Mensagem.deleta_mensagem(codigo)

    return redirect("/comentario")


@app.route("/curtidas/<curtida>")
def curtidas_add(curtida):

    Mensagem.curtidas(curtida)

    return redirect("/comentario")


@app.route("/del-curtidas/<curtidas>")
def curtidas_del(curtidas):

    Mensagem.del_curtidas(curtidas)

    return redirect("/comentario")


@app.route("/login")
def pag_login():    
    
    return render_template("login.html")


@app.route("/post/login", methods=["POST"])
def post_logar():

    usuario = request.form.get("login")
    senha = request.form.get("senha")

    logado = Usuario.logar(usuario, senha)

    if logado == True:
        return redirect("/comentario")
    
    else:
        return redirect("/login")
        

@app.route("/comentario", methods=["GET"])
def comentario():
    if "usuario" in session:
        mensagens = Mensagem.lista_mensagens()

        return render_template("index.html", mensagens = mensagens)
    else:
        return redirect("login.html")


@app.route("/pegacomentario", methods=["GET"])
def pega_comentario():

    return redirect("comentario")


@app.route("/cadastra/usuario", methods=["POST"])
def cadastra_usuario():
    
    login = request.form.get("login")
    usuario = request.form.get("usuario")
    senha = request.form.get("senha")

    Usuario.cadastro_usuario(login, usuario, senha)

    return redirect("/login")


app.secret_key = "zacajaca21"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)