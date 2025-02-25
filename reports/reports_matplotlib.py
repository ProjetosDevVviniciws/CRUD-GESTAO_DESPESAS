# Geração de gráficos

import pandas as pd # Importa a biblioteca pandas para manipulação de dados
import matplotlib.pyplot as plt # Importa matplotlib.pyplot para visualização de gráficos e figuras personalizadas
from database.db_config import get_db_connection # Importa a função para obter a conexão com o banco de dados

def carregar_dados(usuario_id):
    """
    Carrega as despesas de um usuário específico do
    banco de dados para um DataFrame do Pandas
    """
    with get_db_connection() as conn: # Isso garante que a conexão seja fechada automaticamente
        query = """
        SELECT c.nome AS categoria, d.valor
        FROM despesas d
        JOIN categorias c ON d.categoria_id = c.categoria_id 
        WHERE d.usuario_id = %s
        """
        df = pd.read_sql_query(query, conn, params=[usuario_id]) # Filtra pelo usuário
        return df
    
def gerar_relatorio_gastos(usuario_id):
    """
    Gera um gráfico de pizza mostrando a distribuição de 
    gastos por categoria para um usuário específico.
    """
    df = carregar_dados(usuario_id) # Carrega os dados do usuário
    
    if df.empty: # Verifica se há dados para processar
        print("Nenhuma despesa encontrada para gerar o relatório.")
        return
    
    df_grouped = df.groupby("categoria")["valor"].sum() # Agrupa por categoria e soma os valores
    
    def formatar_rotulo(pct, valor_total):
        """
        Formata os rótulos exibindo porcentagem e valor 
        monetário no formato brasileiro.
        """
        valor = pct/100 * valor_total # Calcula o valor correspondente à porcentagem
        
        # Retorna o rótulo com a porcentagem e o valor correspondente
        # Formatação brasileira: vírgula para decimais e ponto para milhares
        if valor > 0:
            return f"{pct:.1f}%\n R${valor:.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        return "" # Se o valor for zero, não exibe rótulo
    
    plt.figure(figsize=(8, 6)) # Cria uma nova figura com tamanho de 8x6 polegadas
    
    # Gera o gráfico de pizza, aplicando a função de formatação nos rótulos
    df_grouped.plot(
        kind="pie", # Tipo do gráfico: pizza (pie)
        autopct=lambda pct: formatar_rotulo(pct, df_grouped.sum()), # Exibe rótulos com % e valores
        color=plt.cm.Set3.colors, # Define uma paleta de cores
        startangle=140
    )
    
    # Personaliza o gráfico
    plt.title(f"Relatório de Gastos por Categoria - Usuário {usuario_id}") # Define o título do gráfico
    plt.ylabel("") # Remove o rótulo padrão do eixo y, pois não é necessário
    plt.legend(df_grouped.index, title="Categorias", loc="center left", bbox_to_anchor=(1, 0.5), fontsize=8)
    plt.tight_layout() # Ajusta o layout para não cortar a legenda
    plt.show() # Exibe o gráfico
    
if __name__ == "__main__": # Verifica se o script está sendo executado diretamente
    try:
        usuario_id = int(input("Digite o ID do usuário:"))
        gerar_relatorio_gastos(usuario_id)
    except ValueError:
        print("ID do usuário inválido. Insira um número inteiro.")
     