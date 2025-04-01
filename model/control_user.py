import datetime
from flask import request
from DATA import conexao as cx_db

class Usuario:
    def cadastro_usuario(login, nome, senha):

        conexao = cx_db.Conexao_db.cria_conexao()

        mycursor = conexao.cursor()

        sql = (""" INSERT INTO tb_usuarios(
                login, nome, senha) VALUES( %s, %s, %s); """)

        valor = (login, nome, senha)

        mycursor.execute(sql, valor)

        conexao.commit()
        mycursor.close()
        conexao.close()