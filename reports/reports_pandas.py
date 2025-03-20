# Exportação de dados

import pandas as pd # Importa a biblioteca pandas para manipulação de dados
from sqlalchemy import create_engine
from urllib.parse import quote_plus  # Importa para codificar a senha corretamente
from database.db_config import get_db_connection # Importa a função para obter a conexão com o banco de dados
from datetime import datetime # Importa a classe datetime para manipulação de data e hora
import traceback # Para exibir erros detalhados
import sys # Para encerrar o programa corretamente

def exportar_para_csv(usuario_id, mes_ano):
    """
    Exporta as despesas de um usuário específico
    para CSV, filtrando por mês.
    """
    try: # Alguma operação que pode gerar erro
        
        def get_db_connection():
            """
            Cria e retorna uma conexão 
            segura com o banco de dados.
            """
            password = quote_plus("@program225X")  # Codifica a senha para evitar erros com caracteres especiais
            engine = create_engine(f"mysql+pymysql://Vinicius:{password}@localhost/gestao_despesas",
                           pool_pre_ping=True,  # Evita erros de conexão perdida
                           connect_args={"charset": "utf8mb4"})  # Garante suporte a caracteres especiais
            return engine.connect()

        query = """
                SELECT c.nome AS Categoria, d.valor, d.data, d.descricao, d.fixa, u.renda_mensal
                FROM despesas d
                JOIN categorias c ON d.categoria_id = c.categoria_id
                JOIN usuarios u ON d.usuario_id = u.usuario_id
                WHERE d.usuario_id = %s AND DATE_FORMAT(d.data, '%%Y-%%m') = %s
            """
            
        # Criando conexão e executando a query
        with get_db_connection() as conn: # Isso garante que a conexão seja fechada automaticamente
            df = pd.read_sql_query(query, conn, params=(usuario_id, mes_ano)) # Executa a consulta e armazena o resultado em um DataFrame
            
        if df.empty:
            print("Nenhuma despesa encontrada para exportar.")
            return
              
        print("Colunas disponíveis no DataFrame: ", df.columns)
            
        # Converte 1 para "Fixa" e 0 para "Variável"
        if 'fixa' in df.columns:
            df['fixa'] = df['fixa'].map({1: 'Fixa', 0: 'Variável'}) # Converte antes de renomear
        else:
                print("Atenção: A coluna 'fixa' não foi encontrada no banco de dados. O tipo de despesa não será incluído.")
            
        # Verifica se há dados antes de gerar o gráfico
        df.rename(columns={
            'renda_mensal': 'Renda Mensal',
            'valor': 'Valor',
            'data': 'Data',
            'descricao': 'Descrição',
            'fixa': 'Tipo'
        }, inplace=True)
        
        df['Data'] = pd.to_datetime(df['Data'])
                        
        # Ordena por data
        df.sort_values(by='Data', inplace=True)
            
        data_atual = datetime.now().strftime("%Y-%m-%d")
        nome_arquivo = f"relatorio_despesas_usuario_{usuario_id}_{mes_ano}_{data_atual}.csv" 
            
        df.to_csv(nome_arquivo, sep=';', index=False, encoding="utf-8-sig", decimal=',') 
        print(f"Relatório exportado com sucesso para {nome_arquivo}")
             
    except Exception:
        print("Erro ao exportar relatório para CSV:")
        traceback.print_exc() # Exibe o rastreamento completo do erro
        
if __name__ == "__main__": # Verifica se o script está sendo executado diretamente
    try:
        usuario_id = int(input("Digite o ID do usuário:"))
        mes_ano = input("Digite o mês no formato YYYY-MM (exemplo: 2025-03): ")
        exportar_para_csv(usuario_id, mes_ano)
    except ValueError:
        print("ID do usuário inválido. Certifique-se de inserir um número inteiro.")
        sys.exit(1)