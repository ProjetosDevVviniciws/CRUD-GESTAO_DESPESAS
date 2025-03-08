# Geração de gráficos

from sqlalchemy import create_engine
from urllib.parse import quote_plus  # Importa para codificar a senha corretamente
import pandas as pd # Importa a biblioteca pandas para manipulação de dados
import matplotlib.pyplot as plt # Importa matplotlib.pyplot para visualização de gráficos e figuras personalizadas
from database.db_config import get_db_connection # Importa a função para obter a conexão com o banco de dados

def get_db_connection(): # Função para conexão com o banco de dados
    password = quote_plus("@program225X")  # Codifica a senha para evitar erros com caracteres especiais
    engine = create_engine(f"mysql+pymysql://Vinicius:{password}@localhost/gestao_despesas",
                           pool_pre_ping=True,  # Evita erros de conexão perdida
                           connect_args={"charset": "utf8mb4"})  # Garante suporte a caracteres especiais
    return engine.connect()

def carregar_dados(usuario_id):
    """
    Carrega as despesas de um usuário específico do banco de dados para um DataFrame do Pandas e
    inclui a coluna 'fixa' para diferenciar despesas fixas e variáveis.
    """
    with get_db_connection() as conn: # Isso garante que a conexão seja fechada automaticamente
        query = """
        SELECT c.nome AS categoria, d.valor, d.fixa
        FROM despesas d
        JOIN categorias c ON d.categoria_id = c.categoria_id 
        WHERE d.usuario_id = %s
        """
        df = pd.read_sql_query(query, conn, params=(usuario_id,)) # Filtra pelo usuário
        
        # Converte 1 para "Fixa" e 0 para "Variável"
        df["Tipo"] = df["fixa"].map({1: "Fixa", 0: "Variável"})
        df.drop(columns=["fixa"], inplace=True) # Remove a coluna fixa original
        
        return df

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

def gerar_relatorio_gastos(usuario_id):
    """
    Gera um gráfico de Pizza e Barras para 
    visualizar os gastos de um usuário específico.
    """
    df = carregar_dados(usuario_id) # Carrega os dados do usuário
    
    if df.empty: # Verifica se há dados para processar
        print("Nenhuma despesa encontrada para gerar o relatório.")
        return
    
    # Gera o gráfico de Pizza - Gastos por Categoria
    plt.figure(figsize=(12, 5)) # Cria uma nova figura com tamanho de 12x5 polegadas
    df_grouped = df.groupby("categoria")["valor"].sum() # Agrupa por categoria e soma os valores
    
    df_grouped.plot(
        kind="pie", # Tipo do gráfico: pizza (pie)
        autopct=lambda pct: formatar_rotulo(pct, df_grouped.sum()), # Exibe rótulos com % e valores
        color=plt.cm.Set3.colors, # Define uma paleta de cores
        startangle=140
    )
    
    plt.title(f"Relatório de Gastos por Categoria - Usuário {usuario_id}") # Define o título do gráfico
    plt.ylabel("") # Remove label do eixo Y
    plt.legend(df_grouped.index, title="Categorias", loc="center left", bbox_to_anchor=(1, 0.5), fontsize=8)
    plt.tight_layout() # Ajusta o layout para não cortar a legenda
    plt.show() # Exibe o gráfico
    
    # Gera o gráfico de Barras - Gastos Fixos vs Variáveis
    plt.figure(figsize=(12, 5)) # Cria uma nova figura com tamanho de 12x5 polegadas
    df_tipo = df.groupby("Tipo")["valor"].sum() # Agrupa valores por tipo (Fixa vs Variável)
    
    # Verifica se há dados antes de gerar o gráfico
    if df_tipo.empty:
        print("Nenhuma despesa fixa ou variável encontrada para gerar o gráfico de Barras.")
        return
    
    df_tipo.plot(
        kind="bar", # Tipo do gráfico: barras (bar)
        color=["#1f77b4", "#ff7f0e"],
        alpha=0.8
    )
    
    for i, valor in enumerate(df_tipo): # Adiciona os valores no topo das Barras
        plt.text(i, valor + (valor * 0.02), f"R${valor:.2f}".replace(".", ","), ha="center", fontsize=10)
    
    plt.xticks(rotation=0)
    plt.title("Relatório de Despesas Fixas vs Variáveis") # Define o título do gráfico
    plt.ylabel("Valor (R$)")
    plt.grid(axis="y", linestyle="--", alpha=0.6) # Linhas de grade no eixo Y   
    plt.tight_layout() # Ajusta os espaçamentos entre os gráficos
    plt.show() # Exibe o gráfico
    
       
if __name__ == "__main__": # Verifica se o script está sendo executado diretamente
    try:
        usuario_id = int(input("Digite o ID do usuário:"))
        gerar_relatorio_gastos(usuario_id)
    except ValueError:
        print("ID do usuário inválido. Insira um número inteiro.")
     