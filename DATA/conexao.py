import mysql.connector

class Conexao_db:

    def cria_conexao():
        mydb = mysql.connector.connect(
            port = 3306,
            host="10.110.134.2",
            user="3ds",
            password="banana",
            database="db_feedback"
        )
        
        return mydb