import datetime
from flask import request
from DATA import conexao as cx_db

class Mensagem:
    def cadastra_menssagem(usuario, mensagem):
        data_hora = datetime.datetime.today()

        conexao_db = cx_db.Conexao_db.cria_conexao()

        valores = (data_hora, usuario, mensagem)
        
        mycursor = conexao_db.cursor()

        sql = ("""INSERT INTO tb_comentarios(
                data_hora, nome, comentario) VALUES( %s, %s, %s);""")

        mycursor.execute(sql, valores)

        conexao_db.commit()
        mycursor.close()
        conexao_db.close()

    def lista_mensagens():
        conexao_db = cx_db.Conexao_db.cria_conexao()

        mycursor = conexao_db.cursor(dictionary=True)

        sql = ("""select data_hora, nome, comentario from tb_comentarios""")

        mycursor.execute(sql)
        resultado = mycursor.fetchall()

        conexao_db.commit()
        mycursor.close()
        conexao_db.close()

        return resultado