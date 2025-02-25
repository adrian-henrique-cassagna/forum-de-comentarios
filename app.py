from flask import Flask, redirect, render_template, request
import datetime
import mysql.connector


app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/post/menssagem", methods=["POST"])
def cadastra_ms():

    usuario = request.form.get("nome")
    data_hora = datetime.datetime.today()
    menssagem = request.form.get("comentario")

    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="db_feedback"
)


    valores = (data_hora, usuario, menssagem)
    
    mycursor = mydb.cursor()

    sql = ("""INSERT INTO tb_comentarios(
                        data_hora, nome, comentario) VALUES( %s, %s, %s)""")

    mycursor.execute(sql, valores)
    
    mydb.commit()
    mycursor.close()
    mydb.close()

    return redirect("/")

if __name__ == __name__:
    app.run(debug=True)