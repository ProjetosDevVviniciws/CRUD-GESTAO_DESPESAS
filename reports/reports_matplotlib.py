# Geração de gráficos

from sqlalchemy import create_engine
from urllib.parse import quote_plus  # Importa para codificar a senha corretamente
import pandas as pd # Importa a biblioteca pandas para manipulação de dados
import matplotlib.pyplot as plt # Importa matplotlib.pyplot para visualização de gráficos e figuras personalizadas
from database.db_config import get_db_connection # Importa a função para obter a conexão com o banco de dados

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

def obter_nome_usuario(usuario_id):
    """
    Obtém o nome do usuário com base no ID.
    """
    with get_db_connection() as conn:
        query = "SELECT nome FROM usuarios WHERE usuario_id = %s"
        df = pd.read_sql_query(query, conn, params=(usuario_id,))
        if not df.empty:
            return df.iloc[0, 0]
        else:
            return "Usuário não encontrado"

def carregar_renda_mensal(usuario_id):
    """
    Obtém a Renda Mensal do usuário.
    """
    with get_db_connection() as conn:
        query = """
        SELECT renda_mensal FROM usuarios WHERE usuario_id = %s
        """
        df = pd.read_sql_query(query,conn, params=(usuario_id,))
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
    nome_usuario = obter_nome_usuario(usuario_id) # Obtém o nome do usuario
    renda_mensal = carregar_renda_mensal(usuario_id) # Obtém a Renda Mensal
    
    if df.empty: 
        print("Nenhuma despesa encontrada para gerar o relatório.")
        return
    
    # Gera o gráfico de Pizza - Gastos por Categoria
    df_grouped = df.groupby("categoria")["valor"].sum() 
    
    df_grouped.plot(
        kind="pie", 
        autopct=lambda pct: formatar_rotulo(pct, df_grouped.sum()),
        textprops={'fontsize': 10.5}, 
        color=plt.cm.Set3.colors, 
        startangle=220
    )
    
    plt.title(f"Relatório de Gastos por Categoria - Usuário: {nome_usuario}", loc="center", fontsize=14) 
    plt.ylabel("")
    plt.legend(df_grouped.index, title="Categorias", loc="center left", bbox_to_anchor=(1.3, 0.5), fontsize=10.5, title_fontsize=13)
    plt.subplots_adjust(left=0.1, right=0.75) 
    plt.tight_layout() 
    plt.show() 
    
    # Gera o gráfico de Barras - Gastos Fixos vs Variáveis 
    df_tipo = df.groupby("Tipo")["valor"].sum() 
    
    if df_tipo.empty:
        print("Nenhuma despesa fixa ou variável encontrada para gerar o gráfico de Barras.")
        return
    
    df_tipo.plot(
        kind="bar", 
        color=["#1f77b4", "#ff7f0e"],
        alpha=1
    )
    
    for i, valor in enumerate(df_tipo): 
        plt.text(i, valor + (valor * 0.02), f"R${valor:.2f}".replace(".", ","), ha="center", fontsize=11)
    
    plt.ylim(0, max(df_tipo) * 1.2)
    plt.title("Relatório de Despesas Fixas vs Variáveis", fontsize=14) 
    plt.xticks(rotation=0, fontsize=11)
    plt.xlabel("Tipo", fontsize=12)
    plt.yticks(rotation=0, fontsize=11)
    plt.ylabel("Valor (R$)", fontsize=12)
    plt.grid(axis="y", linestyle="--", alpha=1)
    plt.subplots_adjust(bottom=0.15)   
    plt.show() 
    
    # Gera Gráfico de Barras - Comparação Gastos Totais vs Renda Mensal
    if not renda_mensal.empty:
        renda_mensal = renda_mensal.iloc[0, 0]  
    else:
        renda_mensal = None  
     
    if renda_mensal is not None:
        total_gastos = df["valor"].sum()
        
        df_comparacao = pd.DataFrame({
            "Categoria": ["Gastos Totais", "Renda Mensal"],
            "Valor": [float(total_gastos), float(renda_mensal)]
        })
        
        df_comparacao["Valor"] = pd.to_numeric(df_comparacao["Valor"])
        
        df_comparacao.set_index("Categoria", inplace=True)
        
        grafico = df_comparacao.plot(
        kind="bar",    
        color=["red" if total_gastos > renda_mensal else "green"], 
        alpha=1
        )
        
        for i, valor in enumerate((total_gastos, renda_mensal)):
            grafico.text(i, valor + (valor * 0.02), f"R${valor:.2f}".replace(".", ","), ha="center", fontsize=11)
        
        plt.ylim(0, max(total_gastos, renda_mensal) * 1.2)
        plt.title("Comparação Gastos Totais vs Renda Mensal", fontsize=14)
        plt.xticks(rotation=0, fontsize=11)
        plt.xlabel("Categoria", fontsize=12)
        plt.yticks(rotation=0, fontsize=11)    
        plt.ylabel("Valor (R$)", fontsize=12)
        plt.grid(axis="y", linestyle="--", alpha=1)
        plt.subplots_adjust(left=0.15, right=0.95, bottom=0.2, top=0.85)
        plt.tight_layout()
        plt.show()
    else:
        print("Renda Mensal não cadastrada para este usuário.")

      
if __name__ == "__main__": # Verifica se o script está sendo executado diretamente
    try:
        usuario_id = int(input("Digite o ID do usuário:"))
        gerar_relatorio_gastos(usuario_id)
    except ValueError:
        print("ID do usuário inválido. Insira um número inteiro.")
     