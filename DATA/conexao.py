import mysql.connector

class Conexao_db:

    def cria_conexao():
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="db_feedback"
        )
        
        return mydb