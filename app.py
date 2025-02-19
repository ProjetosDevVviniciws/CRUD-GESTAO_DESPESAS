# Arquivo principal para a execução do projeto

from crud.usuarios import inserir_usuario, atualizar_usuario, deletar_usuario
from crud.categorias import inserir_categoria, listar_categorias, atualizar_categoria, deletar_categoria
from crud.despesas import inserir_despesa, listar_despesas, atualizar_despesa, deletar_despesa
from reports.reports_pandas import exportar_para_csv
from reports.reports_matplotlib import gerar_relatorio_gastos

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
                menu_despesas()
            case "4":
                menu_exportar_para_csv()
            case "5":
                menu_gerar_relatorio_gastos()
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
        print("3 - Deletar Usuários")
        print("0 - Voltar")
        
        escolha = input("Escolha uma opção: ")
        
        match escolha:
            case "1":
                inserir_usuario()
            case "2":
                atualizar_categoria()
            case "3":
                deletar_usuario()
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
                inserir_categoria()
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

def menu_despesas():
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
                inserir_despesa()
            case "2":
                listar_despesas()
            case "3":
                atualizar_despesa()
            case "4":
                deletar_despesa()
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