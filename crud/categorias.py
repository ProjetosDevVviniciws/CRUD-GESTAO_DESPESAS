# CRUD de categorias

from database.db_config import get_db_connection

def inserir_categoria(nome):
    """"Insere uma nova categoria no Banco de Dados"""
    with get_db_connection() as conn: # Isso garante que a conexão seja fechada automaticamente
        cursor = conn.cursor()
        sql = "INSERT INTO categorias (nome) VALUES (%s)"
        cursor.execute(sql, (nome,))  # Adicionada a vírgula para garantir que seja uma tupla
        conn.commit()
        print("Categoria inserida com sucesso!")

def listar_categorias(): 
    """"Lista todas as categorias existentes"""
    with get_db_connection() as conn: # Isso garante que a conexão seja fechada automaticamente
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM categorias")  
        categorias = cursor.fetchall()
        return categorias

def atualizar_categoria(categoria_id, nome):
    """"Atualiza uma categoria existente"""
    with get_db_connection() as conn: # Isso garante que a conexão seja fechada automaticamente
        cursor = conn.cursor()
        sql = "UPDATE categorias SET nome = %s WHERE categoria_id = %s"
        cursor.execute(sql, (nome, categoria_id))
        conn.commit()
        print("Categoria atualizada com sucesso!")
    
def deletar_categoria(categoria_id):
    """"Deleta uma categoria existente"""
    with get_db_connection() as conn: # Isso garante que a conexão seja fechada automaticamente
        cursor = conn.cursor()
        cursor.execute("DELETE FROM categorias WHERE categoria_id = %s", (categoria_id,))  # Adicionada a vírgula para garantir que seja uma tupla
        conn.commit()
        print("Categoria deletada com sucesso!")