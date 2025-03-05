# Exportação de dados

import pandas as pd # Importa a biblioteca pandas para manipulação de dados
from database.db_config import get_db_connection # Importa a função para obter a conexão com o banco de dados
from datetime import datetime # Importa a classe datetime para manipulação de data e hora
import traceback # Para exibir erros detalhados
import sys # Para encerrar o programa corretamente

def exportar_para_csv(usuario_id):
    """Exporta as despesas de um usuário específico para CSV"""
    try: # Alguma operação que pode gerar erro
        with get_db_connection() as conn: # Isso garante que a conexão seja fechada automaticamente
            query = "SELECT * FROM despesas WHERE usuario_id = %s"
            df = pd.read_sql_query(query, conn, params=(usuario_id,)) # Executa a consulta e armazena o resultado em um DataFrame
            
            # Verifica se há despesas para exportar
            if df.empty:
                print("Nenhuma despesa encontrada para exportar.")
                return
            
            # Renomeia colunas para melhor visualização no Excel
            df.rename(columns={
                'despesa_id': 'ID Despesa',
                'usuario_id': 'ID Usuário',
                'categoria_id': 'ID Categoria',
                'valor': 'Valor',
                'data': 'Data',
                'descricao': 'Descrição',
                'fixa': 'Tipo'
            }, inplace=True)
            
            # Converte 1 para "Fixa" e 0 para "Variável"
            df['Tipo'] = df['fixa'].map({1: 'Fixa', 0: 'Variável'})
            df.drop(columns=['fixa'], inplace=True) # Remove a coluna fixa original
                        
            # Ordena por data
            df.sort_values(by='Data', inplace=True)
            
            data_atual = datetime.now().strftime("%Y-%m-%d") # Obtém a data atual no formato YYYY-MM-DD
            nome_arquivo = f"relatorio_despesas_usuario_{usuario_id}_{data_atual}.csv" # Gera o nome do arquivo CSV
            
            df.to_csv(nome_arquivo, sep=';', index=False, encoding="utf-8-sig", decimal=',') # Salva os dados no arquivo CSV
            print(f"Relatório exportado com sucesso para {nome_arquivo}")
             
    except Exception:
        print("Erro ao exportar relatório para CSV:")
        traceback.print_exc() # Exibe o rastreamento completo do erro
        
if __name__ == "__main__": # Verifica se o script está sendo executado diretamente
    try:
        usuario_id = int(input("Digite o ID do usuário:"))
        exportar_para_csv(usuario_id)
    except ValueError:
        print("ID do usuário inválido. Certifique-se de inserir um número inteiro.")
        sys.exit(1)