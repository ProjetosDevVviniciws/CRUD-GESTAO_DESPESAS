# Conexão com MySQL

import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host= "localhost",
        user="seu_usuario",
        password="sua_senha",
        database="gestao_despesas"
    )