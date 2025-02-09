# CRUD de usuários

from database.db_config import get_db_connection # Importa a função para obter a conexão com o banco de dados

def inserir_usuario(nome, email, cpf):
    """Insere um novo usuário no Banco de Dados"""
    try: # Alguma operação que pode gerar erro
        with get_db_connection() as conn: # Isso garante que a conexão seja fechada automaticamente
            cursor = conn.cursor(dictionary=True)
            sql = "INSERT INTO usuarios (nome, email, cpf) VALUES (%s, %s, %s)"
            cursor.execute(sql, (nome, email, cpf))
            conn.commit()
            print("Usuário inserido com sucesso!")
            return True
    except Exception as e: # O erro é capturado pelo except, e a variável 'e' armazena a exceção
        print(f"Erro ao inserir usuário: {e}")
        return False
    
    
def listar_usuarios():
    """Lista todos os usuários existentes"""
    try: # Alguma operação que pode gerar erro
        with get_db_connection() as conn: # Isso garante que a conexão seja fechada automaticamente
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM usuarios")
            usuarios = cursor.fetchall()
            return usuarios
    except Exception as e: # O erro é capturado pelo except, e a variável 'e' armazena a exceção
        print(f"Erro ao listar usuários: {e}")
        return []
    
def atualizar_usuario(usuario_id, nome, email, cpf):
    """Atualiza um usuário existente"""
    try: # Alguma operação que pode gerar erro
        with get_db_connection() as conn: # Isso garante que a conexão seja fechada automaticamente
            cursor = conn.cursor()
            sql = "UPDATE usuarios SET nome = %s, email = %s, cpf = %s WHERE usuario_id = %s"
            cursor.execute(sql, (nome, email, cpf, usuario_id))
            conn.commit()
            print("Usuário atualizado com sucesso!")
            return True
    except Exception as e: # O erro é capturado pelo except, e a variável 'e' armazena a exceção
        print (f"Erro ao atualizar usuário: {e}")
        return False

def deletar_usuario(usuario_id):
    """Deleta um usuário existente"""
    try: # Alguma operação que pode gerar erro
        with get_db_connection() as conn: # Isso garante que a conexão seja fechada automaticamente
            cursor = conn.cursor()
            cursor.execute("DELETE FROM usuarios WHERE usuario_id = %s", (usuario_id,)) # Adicionada a vírgula para garantir que seja uma tupla
            conn.commit()
            print("Usuário deletado com sucesso!")
            return True
    except Exception as e: # O erro é capturado pelo except, e a variável 'e' armazena a exceção
        print(f"Erro ao deletar usuário: {e}")
        return False