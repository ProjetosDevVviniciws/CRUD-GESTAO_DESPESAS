# CRUD de usuários

from database.db_config import get_db_connection # Importa a função para obter a conexão com o banco de dados

def inserir_usuario(nome, email, cpf, renda_mensal):
    """Insere um novo usuário no Banco de Dados"""
    try: # Alguma operação que pode gerar erro
        with get_db_connection() as conn: # Isso garante que a conexão seja fechada automaticamente
            cursor = conn.cursor(dictionary=True) 
            
            # Verifica se já existe um usuário com o e-mail ou CPF
            cursor.execute("SELECT usuario_id FROM usuarios WHERE email = %s OR cpf = %s", (email, cpf))
            if cursor.fetchone():
                print("Erro: Usuário com esse e-mail ou CPF já cadastrado.")
                return False
            
            # Insere o usuário
            sql = "INSERT INTO usuarios (nome, email, cpf) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (nome, email, cpf, renda_mensal))
            conn.commit()
            print("Usuário inserido com sucesso!")
            return cursor.lastrowid # Retorna o ID do novo usuário
        
    except Exception as e: # O erro é capturado pelo except, e a variável 'e' armazena a exceção
        print(f"Erro ao inserir usuário: {e}")
        return False
    
def atualizar_usuario(usuario_id, nome, email, cpf, renda_mensal):
    """Atualiza um usuário existente"""
    try: # Alguma operação que pode gerar erro
        with get_db_connection() as conn: # Isso garante que a conexão seja fechada automaticamente
            cursor = conn.cursor(dictionary=True)
            
            # Verifica se o usuário existe
            cursor.execute("SELECT usuario_id FROM usuarios WHERE usuario_id = %s", (usuario_id,)) # Adicionada a vírgula para garantir que seja uma tupla
            if not cursor.fetchone():
                print("Erro: Usuário não encontrado!")
                return False
            
            # Verifica se já existe outro usuário com esse e-mail ou CPF
            cursor.execute("SELECT usuario_id FROM usuarios WHERE (email = %s OR cpf = %s) AND usuario_id != %s", (email, cpf, usuario_id))
            if cursor.fetchone():
                print("Erro: Já existe outro usuário com esse e-mail ou CPF!")
                return False
            
            # Atualiza o usuário
            sql = "UPDATE usuarios SET nome = %s, email = %s, cpf = %s, renda_mensal = %s WHERE usuario_id = %s"
            cursor.execute(sql, (nome, email, cpf, renda_mensal, usuario_id))
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
            cursor = conn.cursor(dictionary=True)
            
            # Verifica se o usuário existe antes de deletar
            cursor.execute("SELECT usuario_id FROM usuarios WHERE usuario_id = %s", (usuario_id,)) # Adicionada a vírgula para garantir que seja uma tupla
            if not cursor.fetchone():
                print("Erro: Usuário não encontrado!")
                return False
            
            # Deleta o usuário
            cursor.execute("DELETE FROM usuarios WHERE usuario_id = %s", (usuario_id,)) 
            conn.commit()
            print("Usuário deletado com sucesso!")
            return True
        
    except Exception as e: # O erro é capturado pelo except, e a variável 'e' armazena a exceção
        print(f"Erro ao deletar usuário: {e}")
        return False