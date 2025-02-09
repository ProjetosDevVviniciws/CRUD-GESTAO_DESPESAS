# CRUD de usuários

import bcrypt
from database.db_config import get_db_connection

def hash_senha(senha):
    """Hash da senha usando bcrypt"""
    return bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())

def inserir_usuario(nome, email, senha):
    """Insere um novo usuário no Banco de Dados"""
    with get_db_connection() as conn: # Isso garante que a conexão seja fechada automaticamente
        cursor = conn.cursor(dictionary=True)
        sql = "INSERT INTO usuarios (nome, email, senha) VALUES (%s, %s, %s)"
        cursor.execute(sql, (nome, email, senha))
        conn.commit()
        print("Usuário inserido com sucesso!")
    
def listar_usuarios():
    """Lista todos os usuários existentes"""
    with get_db_connection() as conn: # Isso garante que a conexão seja fechada automaticamente
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuarios")
        usuarios = cursor.fetchall()
        return usuarios
    
def atualizar_usuario(usuario_id, nome, email, senha):
    """Atualiza um usuário existente"""
    with get_db_connection() as conn: # Isso garante que a conexão seja fechada automaticamente
        cursor = conn.cursor()
        sql = "UPDATE usuarios SET nome = %s, email = %s, senha = %s WHERE usuario_id = %s"
        cursor.execute(sql, (nome, email, senha, usuario_id))
        conn.commit()
        print("Usuário atualizado com sucesso!")

def deletar_usuario(usuario_id):
    """Deleta um usuário existente"""
    with get_db_connection() as conn: # Isso garante que a conexão seja fechada automaticamente
        cursor = conn.cursor()
        cursor.execute("DELETE FROM usuarios WHERE usuario_id = %s", (usuario_id,)) # Adicionada a vírgula para garantir que seja uma tupla
        conn.commit()
        print("Usuário deletado com sucesso!")