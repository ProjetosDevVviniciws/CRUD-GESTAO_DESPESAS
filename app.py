# Arquivo principal para a execução do projeto

from crud.usuarios import inserir_usuario, atualizar_usuario, deletar_usuario
from crud.categorias import inserir_categoria, listar_categorias, atualizar_categoria, deletar_categoria
from crud.despesas import inserir_despesa, listar_despesas, atualizar_despesa, deletar_despesa
from reports.reports_pandas import exportar_para_csv
from reports.reports_matplotlib import gerar_relatorio_gastos
from datetime import datetime

# ========================= MENU PRINCIPAL =========================

def menu_principal():
    while True:
        print("\n=== Menu Principal ===")
        print("1 - Gerenciar Usuários")
        print("2 - Gerenciar Categorias")
        print("3 - Gerenciar Despesas")
        print("4 - Exportar para CSV")
        print("5 - Gerar Relatório de Gastos")
        print("0 - Sair")
        
        escolha = input("Escolha uma opção: ")
        
        match escolha:
            case "1":
                menu_usuarios()
            case "2":
                menu_categorias()
            case "3":
                usuario_id = input("Digite o ID do usuário: ")
                menu_despesas(usuario_id)
            case "4":
                usuario_id = input("Digite o ID do usuário: ")
                menu_exportar_para_csv(usuario_id)
            case "5":
                usuario_id = input("Digite o ID do usuário: ")
                menu_gerar_relatorio_gastos(usuario_id)
            case "0":
                print("Saindo...")
                break
            case _:
                print("Opção inválida. Tente novamente.")

# ========================= MENU USUÁRIOS =========================

def menu_usuarios():
    while True:
        print("\n=== Menu Usuários ===")
        print("1 - Inserir Usuário")
        print("2 - Atualizar Usuário")
        print("3 - Deletar Usuário")
        print("0 - Voltar")
        
        escolha = input("Escolha uma opção: ")
        
        match escolha:
            case "1":
                nome = str(input("Digite o nome do usuário: "))
                email = input("Digite o email do usuário: ")
                cpf = input("Digite o CPF do usuário: ")
                inserir_usuario(nome, email, cpf)
                
            case "2":
                usuario_id = int(input("Digite o ID do usuário: "))
                nome = input("Digite o nome do usuário: ")
                email = input("Digite o e-mail do usuário: ")
                cpf = int(input("Digite o CPF do usuário: "))
                atualizar_usuario(usuario_id, nome, email, cpf)
                
            case "3":
                usuario_id = int(input("Digite o ID do usuário: "))
                deletar_usuario(usuario_id)
                
            case "0":
                break
            
            case _:
                print("Opção inválida. Tente novamente.")

# ========================= MENU CATEGORIAS =========================

def menu_categorias():
    while True:
        print("\n=== Menu Categorias ===")
        print("1 - Inserir Categoria")
        print("2 - Listar Categorias")
        print("3 - Atualizar Categoria")
        print("4 - Deletar Categoria")
        print("0 - Voltar")
        
        escolha = input("Escolha um opção: ")
        
        match escolha:
            case "1":
                nome = input("Digite o nome da categoria: ")
                inserir_categoria(nome)
                
            case "2":
                listar_categorias()
                
            case "3":
                atualizar_categoria()
                
            case "4":
                deletar_categoria()
                
            case "0":
                
                break
            
            case _:
                print("Opção inválida. Tente novamente.")
        
# ========================= MENU DESPESAS =========================

def menu_despesas(usuario_id):
    while True:
        print("\n=== Menu Despesas ===")
        print("1 - Inserir Despesa")
        print("2 - Listar Despesas")
        print("3 - Atualizar Despesa")
        print("4 - Deletar Despesa")
        print("0 - Voltar")
        
        escolha = input("Escolha uma opção: ")
        
        match escolha:
            case "1":
                usuario_id = int(input("Digite o ID do usuário: "))
                nome = input("Digite o nome da despesa: ")
                valor = float(input("Digite o valor da despesa: "))
                
                data = input("Digite a data da despesa (YYYY-MM-DD): ")
                datetime.strptime(data, "%Y-%m-%d")
                
                descricao = input("Digite a descição da despesa: ")
                inserir_despesa(usuario_id, nome, valor, data, descricao)
                
            case "2":
                usuario_id = int(input("Digite o ID do usuário: "))
                despesas = listar_despesas(usuario_id) # Recebe a despesa do banco
                
                if despesas:
                    print("\n=== Despesas Cadastradas ===")
                    for despesa in despesas:
                        print(f"ID: {despesa['despesa_id']} | Categoria: {despesa['categoria_nome']} | "
                              f"Valor: R${despesa['valor']:.2f} | Data: {despesa['data']} | "
                              f"Descrição: {despesa['descricao']}")
                else:
                    print("Nenhuma despesa encontrada para este usuário.")
                    
            case "3":
                try:
                    despesa_id = int(input("Digite o ID da despesa: "))
                    categoria_id = int(input("Digite o ID da categoria: "))
                    valor = float(input("Digite o novo valor da despesa: "))
                    
                    data = input("Digite a data nova da despesa (YYYY-MM-DD): ")
                    datetime.strptime(data, "%Y-%m-%d") # Valida o formato da data
                    
                    descricao = input("Digite a nova descrição da despesa: ")
                    
                    atualizar_despesa(despesa_id, categoria_id, valor, data, descricao)
                
                except ValueError as e:
                    print(f"Erro: {e}. Certifique-se de inserir números válidos e data no formato correto.")
                
            case "4":
                despesa_id = input("Digite o ID da despesa: ")
                deletar_despesa(despesa_id)
                
            case "0":
                
                break
            
            case _:
                print("Opção inválida. Tente novamente.")

# ========================= MENU EXPORTAR CSV =========================

def menu_exportar_para_csv():
    while True:
        print("\n=== Menu Exportar para CSV ===")
        print("1 - Exportar para CSV")
        print("0 - Voltar")
        
        escolha = input("Escolha uma opção: ")
        
        match escolha:
            case "1":
                exportar_para_csv()
            case "0":
                break
            case _:
                print("Opção inválida. Tente novamente.")
                
# ========================= MENU GERAR RELATÓRIO DE GASTOS =========================

def menu_gerar_relatorio_gastos():
    while True:
        print("\n=== Menu Gerar Relatório de Gastos ===")
        print("1 - Gerar Relatório de Gastos")
        print("0 - Voltar")
        
        escolha  = input("Escolha uma opção: ")
        
        match escolha:
            case "1":
                gerar_relatorio_gastos()
            case "0":
                break
            case _:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu_principal()