# Geração de gráficos

import pandas as pd # Importa a biblioteca pandas para manipulação de dados
import matplotlib.pyplot as plt # Importa matplotlib.pyplot para visualização de gráficos e figuras personalizadas
from database.db_config import get_db_connection # Importa a função para obter a conexão com o banco de dados

def carregar_dados(usuario_id):
    """Carrega as despesas de um usuário específico do banco de dados para um DataFrame do Pandas"""
    with get_db_connection() as conn: # Isso garante que a conexão seja fechada automaticamente
        query = "SELECT categoria, valor FROM despesas WHERE usuario_id = %s"
        df = pd.read_sql_query(query, conn, params=[usuario_id]) # Filtra pelo usuário
        return df
    
def gerar_relatorio_gastos(usuario_id):
    """Gera um gráfico de pizaa dos gastos por categoria"""    