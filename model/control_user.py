import datetime
from flask import request
from DATA import conexao as cx_db
from hashlib import sha256

class Usuario:
    def cadastro_usuario(login, nome, senha):

        senha = sha256(senha.encode()).hexdigest()

        conexao = cx_db.Conexao_db.cria_conexao()

        mycursor = conexao.cursor()

        sql = (""" INSERT INTO tb_usuarios(
                login, nome, senha) VALUES( %s, %s, %s); """)

        valor = (login, nome, senha)

        mycursor.execute(sql, valor)

        conexao.commit()
        mycursor.close()
        conexao.close()

    
    def logar(login, senha):
        senha = sha256(senha.encode()).hexdigest()

        conexao = cx_db.Conexao_db.cria_conexao()

        mycursor = conexao.cursor()

        sql = (""" SELECT login, senha FROM tb_usuarios WHERE login = %s AND senha = %s """)

        valor = (login, senha)

        mycursor.execute(sql, valor)

        resultado = mycursor.fetchone()