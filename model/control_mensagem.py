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

        sql = ("""select data_hora, nome, comentario, cod_comentario, curtidas from tb_comentarios""")

        mycursor.execute(sql)
        resultado = mycursor.fetchall()

        conexao_db.commit()
        mycursor.close()
        conexao_db.close()

        return resultado
    
    def deleta_mensagem(codigo):
        conexao = cx_db.Conexao_db.cria_conexao()

        mycursor = conexao.cursor()

        sql = (""" DELETE from tb_comentarios where cod_comentario = %s; """)

        valor = (codigo,)

        mycursor.execute(sql, valor)

        conexao.commit()
        mycursor.close()
        conexao.close()

    def curtidas(codigo):
        conexao = cx_db.Conexao_db.cria_conexao()

        mycursor = conexao.cursor()

        sql = (""" UPDATE tb_comentarios SET curtidas = curtidas + 1 WHERE cod_comentario = %s; """)

        valor = (codigo,)

        mycursor.execute(sql, valor)

        conexao.commit()
        mycursor.close()
        conexao.close()

    def del_curtidas(codigo):
        conexao = cx_db.Conexao_db.cria_conexao()

        mycursor = conexao.cursor()

        sql = (""" UPDATE tb_comentarios SET curtidas = curtidas - 1 WHERE cod_comentario = %s; """)

        valor = (codigo,)

        mycursor.execute(sql, valor)

        conexao.commit()
        mycursor.close()
        conexao.close()