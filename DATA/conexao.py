import mysql.connector

class Conexao_db:

    def cria_conexao():
        mydb = mysql.connector.connect(
            port = 27974,
            host="dbgodofredo-alexstocco-93db.b.aivencloud.com",
            user="3ds",
            password="banana",
            database="db_feedback"
        )
        
        return mydb