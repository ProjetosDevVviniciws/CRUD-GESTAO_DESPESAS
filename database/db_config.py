# Conexão com MySQL

import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host= "localhost",
        user="Vinicius",
        password="@program225X",
        database="gestao_despesas"
    )