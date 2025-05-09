# CRUD de categorias

from database.db_config import get_db_connection # Importa a função para obter a conexão com o banco de dados

def inserir_categoria(nome, usuario_id):
    """Insere uma nova categoria vinculada a um usuário no Banco de Dados (evita duplicatas)"""
    try: # Alguma operação que pode gerar erro
        
        with get_db_connection() as conn: # Isso garante que a conexão seja fechada automaticamente
            cursor = conn.cursor(dictionary=True)
            
            # Verifica se a categoria já existe:
            cursor.execute("SELECT categoria_id FROM categorias WHERE nome = %s AND usuario_id = %s", (nome, usuario_id,)) 
            categoria = cursor.fetchone()
            
            if categoria:
                print(f"A categoria '{nome}' já existe para este usuário.")
                return categoria['categoria_id'] # Obtém o ID da nova categoria
            else:
                
                # Se não existir, cria a categoria
                cursor.execute("INSERT INTO categorias (nome, usuario_id) VALUES (%s, %s)", (nome, usuario_id))
                conn.commit()
                categoria_id = cursor.lastrowid # Obtém o ID da nova categoria
                
                print("Categoria inserida com sucesso!")
                return categoria_id
        
    except Exception as e:  # O erro é capturado pelo except, e a variável 'e' armazena a exceção
        if "Duplicate entry" in str(e):
            print(f"A categoria '{nome}' já existe para este usuário.")
        else:
            print(f"Erro ao inserir categoria: {e}")
        return False

def listar_categorias(usuario_id): 
    """Lista todas as categorias existentes de um usuário específico"""
    try: # Alguma operação que pode gerar erro
        with get_db_connection() as conn: # Isso garante que a conexão seja fechada automaticamente
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT categoria_id, nome FROM categorias WHERE usuario_id = %s", (usuario_id,)) # Adicionada a vírgula para garantir que seja uma tupla
            return cursor.fetchall()
        
    except Exception as e: # O erro é capturado pelo except, e a variável 'e' armazena a exceção
        print(f"Erro ao listar categorias: {e}")
        return []

def atualizar_categoria(usuario_id, categoria_id, nome):
    """Atualiza uma categoria existente de um usuário específico"""
    try: # Alguma operação que pode gerar erro
        with get_db_connection() as conn: # Isso garante que a conexão seja fechada automaticamente
            cursor = conn.cursor()
            
            # Verifica se a cetegoria existe antes de atualizar
            cursor.execute("SELECT categoria_id FROM categorias WHERE categoria_id = %s AND usuario_id = %s", (categoria_id, usuario_id))
            if not cursor.fetchone():
                print(f"Erro: Categoria não encontrada!")
                return False
            
            # Atualiza a categoria
            sql = "UPDATE categorias SET nome = %s WHERE categoria_id = %s AND usuario_id = %s"
            cursor.execute(sql, (nome, categoria_id, usuario_id))
            conn.commit()
            print("Categoria atualizada com sucesso!")
            return True
        
    except Exception as e: # O erro é capturado pelo except, e a variável 'e' armazena a exceção
        print(f"Erro ao atualizar categoria: {e}")
        return False
    
def deletar_categoria(usuario_id, categoria_id):
    """Deleta uma categoria existente de um usuário específico"""
    try: # Alguma operação que pode gerar erro
        with get_db_connection() as conn: # Isso garante que a conexão seja fechada automaticamente
            cursor = conn.cursor()
            
            # Verifica se a categoria existe antes de deletar
            cursor.execute("SELECT categoria_id FROM categorias WHERE categoria_id = %s AND usuario_id = %s", (categoria_id, usuario_id)) 
            if not cursor.fetchone():
                print(f"Erro: Categoria não encontrada!")
                return False
            
            # Deleta a categoria
            cursor.execute("DELETE FROM categorias WHERE categoria_id = %s AND usuario_id = %s", (categoria_id, usuario_id)) 
            conn.commit()
            print("Categoria deletada com sucesso!")
            return True
        
    except Exception as e: # O erro é capturado pelo except, e a variável 'e' armazena a exceção
        print(f"Erro ao deletar categoria: {e}")
        return False