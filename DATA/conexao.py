import mysql.connector

v1 = 0

class Conexao_db:

    def cria_conexao():
        if(v1 == 0):
                mydb = mysql.connector.connect(
                    port = 3306,
                    host="localhost",
                    user="3ds",
                    password="banana",
                    database="db_feedback"
                )
            
                return mydb
    
        def cria_conexao():
            if v1 == 1:
                mydb = mysql.connector.connect(
                    port = 27974,
                    host="dbgodofredo-alexstocco-93db.b.aivencloud.com",
                    user="3ds",
                    password="banana",
                    database="db_feedback"
                )
                
                return mydb