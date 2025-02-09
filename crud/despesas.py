# CRUD de despesas

from database.db_config import get_db_connection # Importa a função para obter a conexão com o banco de dados

def inserir_despesa(usuario_id, categoria_id, valor, data, descricao):
    """Insere uma nova despesa no Banco de Dados"""
    try: # Alguma operação que pode gerar erro
        with get_db_connection() as conn: # Isso garante que a conexão seja fechada automaticamente
            cursor = conn.cursor()
            sql = "INSERT INTO despesas (usuario_id, categoria_id, valor, data, descricao) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (usuario_id, categoria_id, valor, data, descricao))
            conn.commit()
            print("Despesa inserida com sucesso!")
            return True
    except Exception as e: # O erro é capturado pelo except, e a variável 'e' armazena a exceção
        print(f"Erro ao inserir despesa: {e}")
        return False
    
def listar_despesas(usuario_id):
    """Lista todas as despesas de um usuário específico"""
    try: # Alguma operação que pode gerar erro
        with get_db_connection() as conn: # Isso garante que a conexão seja fechada automaticamente
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM despesas WHERE usuario_id = %s", (usuario_id,)) # Adicionada a vírgula para garantir que seja uma tupla
            despesas = cursor.fetchall()
            return despesas
    except Exception as e: # O erro é capturado pelo except, e a variável 'e' armazena a exceção
        print(f"Erro ao listar despesas: {e}")
        return []

def atualizar_despesa(despesa_id, categoria_id, valor, data, descricao):
    """Atualiza uma despesa existente"""
    try: # Alguma operação que pode gerar erro
        with get_db_connection() as conn: # Isso garante que a conexão seja fechada automaticamente
            cursor = conn.cursor()
            sql = "UPDATE despesas SET categoria_id = %s, valor = %s, data = %s, descricao = %s WHERE despesa_id = %s"
            cursor.execute(sql, (categoria_id, valor, data, descricao, despesa_id))
            conn.commit()
            print("Despesa atualizada com sucesso!")
            return True
    except Exception as e: # O erro é capturado pelo except, e a variável 'e' armazena a exceção
        print(f"Erro ao atualizar despesa: {e}")
        return False
    
def deletar_despesa(despesa_id):
    """Deleta uma despesa existente"""
    try: # Alguma operação que pode gerar erro
        with get_db_connection() as conn: # Isso garante que a conexão seja fechada automaticamente
            cursor = conn.cursor()
            cursor.execute("DELETE FROM despesas WHERE despesa_id = %s", (despesa_id,)) # Adicionada a vírgula para garantir que seja uma tupla
            conn.commit()
            print("Despesa deletada com sucesso!")
            return True
    except Exception as e: # O erro é capturado pelo except, e a variável 'e' armazena a exceção
        print(f"Erro ao deletar despesa: {e}")
        return False