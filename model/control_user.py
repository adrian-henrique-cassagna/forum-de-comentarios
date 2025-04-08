import datetime
from flask import session
from DATA.conexao import Conexao_db as cx_db
from hashlib import sha256

class Usuario:
    def cadastro_usuario(login, nome, senha):

        senha = sha256(senha.encode()).hexdigest()

        conexao = cx_db.cria_conexao()

        mycursor = conexao.cursor()

        sql = (""" INSERT INTO tb_usuarios(
                login, nome, senha) VALUES( %s, %s, %s); """)

        valor = (login, nome, senha)

        mycursor.execute(sql, valor)

        conexao.commit()
        conexao.close()
    
    def logar(login, senha):

        senha = sha256(senha.encode()).hexdigest()

        conexao = cx_db.cria_conexao()

        mycursor = conexao.cursor(dictionary=True)

        sql = (""" SELECT login, nome FROM tb_usuarios WHERE login = %s AND senha = %s """)

        valor = (login, senha)

        mycursor.execute(sql, valor)

        resultado = mycursor.fetchone()

        conexao.close()

        if resultado:

            session["usuario"] = resultado["login"]
            session["nome"] = resultado["nome"]

            return True
        else:
            return False