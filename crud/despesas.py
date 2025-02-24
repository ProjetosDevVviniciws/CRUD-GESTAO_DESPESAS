# CRUD de despesas

from database.db_config import get_db_connection # Importa a função para obter a conexão com o banco de dados

def inserir_despesa(usuario_id, nome, valor, data, descricao):
    """Insere uma nova despesa no Banco de Dados"""
    try: # Alguma operação que pode gerar erro
        with get_db_connection() as conn: # Isso garante que a conexão seja fechada automaticamente
            cursor = conn.cursor(dictionary=True)
            
            # Verifica se a categoria existe e obtém o ID
            cursor.execute("SELECT categoria_id FROM categorias WHERE nome = %s AND usuario_id = %s", (nome, usuario_id))
            categoria = cursor.fetchone()
              
            if not categoria:
                # Se a categoria não existir, cria automaticamente
                cursor.execute("INSERT INTO categorias (usuario_id, nome) VALUES (%s, %s)", (usuario_id, nome))
                conn.commit()
                categoria_id = cursor.lastrowid # Obtém o ID da categoria recém-criada
            else:
                categoria_id = categoria['categoria_id'] # Obtém o ID da categoria existente
            
            # Insere a despesa
            sql = "INSERT INTO despesas (usuario_id, categoria_id, valor, data, descricao) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (usuario_id, categoria_id, valor, data, descricao))
            conn.commit()
            print("Despesa inserida com sucesso!")
            return True
        
    except Exception as e: # O erro é capturado pelo except, e a variável 'e' armazena a exceção
        # Captura erro de chave úncia (se a despesa for duplicada)
        if "Duplicate entry" in str(e):
            print("Despesa duplicada!")
        else:
            print(f"Erro ao inserir despesa: {e}")
            return False 
    
def listar_despesas(usuario_id):
    """Lista todas as despesas de um usuário específico, incluindo a categoria"""
    try: # Alguma operação que pode gerar erro
        with get_db_connection() as conn: # Isso garante que a conexão seja fechada automaticamente
            cursor = conn.cursor(dictionary=True)
            query = """
                SELECT d.despesa_id, d.usuario_id, d.categoria_id, d.valor, d.data, d.descricao, c.nome AS categoria_nome
                FROM despesas AS d
                JOIN categorias AS c ON d.categoria_id = c.categoria_id
                WHERE d.usuario_id = %s    
            """
            cursor.execute(query, (usuario_id,)) 
            despesas = cursor.fetchall()
            return despesas
        
    except Exception as e: # O erro é capturado pelo except, e a variável 'e' armazena a exceção
        print(f"Erro ao listar despesas: {e}")
        return []

def atualizar_despesa(despesa_id, categoria_id, valor, data, descricao):
    """Atualiza uma despesa existente"""
    try: # Alguma operação que pode gerar erro
        with get_db_connection() as conn: # Isso garante que a conexão seja fechada automaticamente
            cursor = conn.cursor(dictionary=True)
            
            # Verifica se a despesa existe
            cursor.execute("SELECT despesa_id FROM despesas WHERE despesa_id = %s", (despesa_id,))
            if not cursor.fetchone():
                print(f"Despesa não encontrada!")
                return False
            
            # Verifica se a categoria existe
            cursor.execute("SELECT categoria_id FROM categorias WHERE categoria_id  = %s", (categoria_id,))
            if not cursor.fetchone():
                print(f"Categoria não encontrada!")
                return False
            
            # Atualiza a despesa
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
            cursor = conn.cursor(dictionary=True)
            
            # Verifica se a despesa existe antes de tentar delatar
            cursor.execute("SELECT despesa_id FROM despesas WHERE despesa_id = %s", (despesa_id,)) # Adicionada a vírgula para garantir que seja uma tupla
            if not cursor.fetchone():
                print("Erro: Despesa não encontrada!")
                return False
            
            # Deleta a despesa
            cursor.execute("DELETE FROM despesas WHERE despesa_id = %s", (despesa_id, )) # Adicionada a vírgula para garantir que seja uma tupla
            conn.commit()
            print("Despesa deletada com sucesso!")
            return True
        
    except Exception as e: # O erro é capturado pelo except, e a variável 'e' armazena a exceção
        print(f"Erro ao deletar despesa: {e}")
        return False