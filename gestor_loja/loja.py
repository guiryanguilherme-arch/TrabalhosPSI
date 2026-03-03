from funcoes import *
from datetime import datetime

# ----------------------------
# LISTAS DE CONTAS
# ----------------------------
funcionarios = []
utilizadores = []

# ----------------------------
# REGISTRAR FUNCIONÁRIO
# ----------------------------
def registrar_funcionario():
    nome = input("Nome do funcionário: ")
    if not nome.replace(" ", "").isalpha():
        print("Nome inválido. Apenas letras são permitidas.")
        return
    for f in funcionarios:
        if f["nome"].lower() == nome.lower():
            print("Funcionário já registrado.")
            return
    senha = input("Senha: ")
    if not senha:
        print("Senha inválida.")
        return
    funcionarios.append({"nome": nome, "senha": senha})
    print(f"Funcionário '{nome}' registrado com sucesso!")

# ----------------------------
# LOGIN FUNCIONÁRIO
# ----------------------------
def login_funcionario():
    nome = input("Nome: ")
    senha = input("Senha: ")
    for f in funcionarios:
        if f["nome"].lower() == nome.lower() and f["senha"] == senha:
            print(f"Login de funcionário '{nome}' realizado!")
            menu_funcionario()
            return
    print("Dados incorretos.")

# ----------------------------
# MENU FUNCIONÁRIO
# ----------------------------
def menu_funcionario():
    while True:
        print("\n=== ÁREA DO FUNCIONÁRIO ===")
        print("1 - Ver produtos")
        print("2 - Adicionar produto")
        print("3 - Vender produto")
        print("4 - Valor total da loja")
        print("5 - Alertar stock baixo")
        print("6 - Produto em destaque")
        print("7 - Ver hora atual")
        print("8 - Horário de trabalho")
        print("0 - Sair")

        op = input("Escolha: ")
        if op == "1":
            listar_produtos()
        elif op == "2":
            adicionar_produto()
        elif op == "3":
            vender_produto()
        elif op == "4":
            valor_total()
        elif op == "5":
            alerta_stock_baixo()
        elif op == "6":
            produto_destaque()
        elif op == "7":
            ver_hora()
        elif op == "8":
            horario_funcionario()
        elif op == "0":
            break
        else:
            print("Opção inválida.")

# ----------------------------
# CRIAR CONTA CLIENTE
# ----------------------------
def criar_conta():
    nome = input("Nome: ")
    if not nome.replace(" ", "").isalpha():
        print("Nome inválido. Apenas letras são permitidas.")
        return
    for u in utilizadores:
        if u["nome"].lower() == nome.lower():
            print("Conta já existente.")
            return
    senha = input("Senha: ")
    if not senha:
        print("Senha inválida.")
        return
    try:
        saldo = float(input("Saldo inicial: "))
        if saldo < 0:
            print("Saldo inválido.")
            return
    except ValueError:
        print("Saldo inválido.")
        return
    utilizadores.append({"nome": nome, "senha": senha, "saldo": saldo, "carrinho": [], "historico": []})
    print(f"Conta de cliente '{nome}' criada com sucesso!")

# ----------------------------
# LOGIN CLIENTE
# ----------------------------
def login_utilizador():
    nome = input("Nome: ")
    senha = input("Senha: ")
    for u in utilizadores:
        if u["nome"].lower() == nome.lower() and u["senha"] == senha:
            print(f"Login de cliente '{nome}' realizado!")
            menu_cliente(u)
            return
    print("Dados incorretos.")

# ----------------------------
# MENU CLIENTE
# ----------------------------
def menu_cliente(utilizador):
    while True:
        print("\n=== ÁREA DO CLIENTE ===")
        print("1 - Ver produtos")
        print("2 - Ver produtos por secção")
        print("3 - Adicionar ao carrinho")
        print("4 - Remover do carrinho")
        print("5 - Ver carrinho")
        print("6 - Finalizar compra")
        print("7 - Ver dados da conta")
        print("8 - Ver histórico de compras")
        print("9 - Ver hora atual")
        print("0 - Sair")

        op = input("Escolha: ")
        if op == "1":
            listar_produtos()
        elif op == "2":
            secao = input(f"Qual secção deseja ver? ({', '.join(secoes)}): ")
            listar_por_secao(secao)
        elif op == "3":
            listar_produtos()  # Mais lógico: mostrar produtos antes de adicionar
            adicionar_ao_carrinho(utilizador)
        elif op == "4":
            remover_do_carrinho(utilizador)
        elif op == "5":
            ver_carrinho(utilizador)
        elif op == "6":
            finalizar_compra(utilizador)
        elif op == "7":
            ver_dados_conta(utilizador)
        elif op == "8":
            ver_historico(utilizador)
        elif op == "9":
            ver_hora()
        elif op == "0":
            break
        else:
            print("Opção inválida.")

# ----------------------------
# FUNÇÕES AUXILIARES
# ----------------------------
def ver_hora():
    agora = datetime.now()
    print("Hora atual:", agora.strftime("%d/%m/%Y %H:%M:%S"))

def horario_funcionario():
    print("Horário de trabalho: Segunda a Sexta, das 09:00 às 18:00")

# ----------------------------
# MAIN
# ----------------------------
def main():
    while True:
        print("\n=== FNAC ===")
        print("1 - Registrar Funcionário")
        print("2 - Login Funcionário")
        print("3 - Criar Conta Cliente")
        print("4 - Login Cliente")
        print("0 - Sair")

        op = input("Escolha: ")
        if op == "1":
            registrar_funcionario()
        elif op == "2":
            login_funcionario()
        elif op == "3":
            criar_conta()
        elif op == "4":
            login_utilizador()
        elif op == "0":
            print("Até logo!")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()