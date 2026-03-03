# Importa a lista de produtos e secções do ficheiro dados.py
from dados import produtos, secoes

# Importa datetime para trabalhar com data e hora
from datetime import datetime


# ----------------------------
# LISTAR TODOS OS PRODUTOS
# ----------------------------
def listar_produtos():
    # Verifica se a lista está vazia
    if not produtos:
        print("Nenhum produto disponível.")
        return  # Sai da função se não houver produtos

    print("\n=== PRODUTOS ===")

    # Percorre todos os produtos da lista
    for p in produtos:
        # p é uma tupla: (id, nome, secao, preco, stock)
        print(f"[{p[0]}] {p[1]} | {p[2]} | {p[3]:.2f}€ | Stock: {p[4]}")

    # Soma total das unidades em stock
    total_unidades = sum(p[4] for p in produtos)

    # Mostra estatísticas
    print(f"Tipos de produtos: {len(produtos)}")
    print(f"Total de unidades em stock: {total_unidades}")


# ----------------------------
# LISTAR POR SECÇÃO
# ----------------------------
def listar_por_secao(secao):
    encontrou = False  # Variável para verificar se encontrou produtos

    print(f"\n=== SECÇÃO: {secao.capitalize()} ===")

    # Percorre todos os produtos
    for p in produtos:
        # Compara a secção ignorando maiúsculas/minúsculas
        if p[2].lower() == secao.lower():
            print(f"[{p[0]}] {p[1]} | {p[3]:.2f}€ | Stock: {p[4]}")
            encontrou = True  # Marca que encontrou pelo menos um

    # Caso não encontre nenhum produto
    if not encontrou:
        print("Nenhum produto encontrado.")


# ADICIONAR PRODUTO
# ----------------------------
def adicionar_produto():
    try:
        # Pede o nome do produto
        nome = input("Nome: ").strip()

        # Verifica se o nome é válido
        if not nome:
            print("Nome inválido.")
            return

        # Verifica se já existe produto com esse nome
        for p in produtos:
            if p[1].lower() == nome.lower():
                print("Produto já existe.")
                return

        # Pede a secção e valida se está na lista de secções
        secao = input(f"Secção ({', '.join(secoes)}): ").capitalize()
        if secao not in secoes:
            print("Secção inválida.")
            return

        # Pede preço e converte para float
        preco = float(input("Preço: "))
        if preco <= 0:
            print("Preço inválido.")
            return

        # Pede stock e converte para inteiro
        stock = int(input("Stock: "))
        if stock < 0:
            print("Stock inválido.")
            return

        # Gera novo ID automaticamente (maior ID + 1)
        novo_id = max(p[0] for p in produtos) + 1 if produtos else 1

        # Adiciona novo produto à lista
        produtos.append((novo_id, nome, secao, preco, stock))

        print("Produto adicionado com sucesso!")

    # Captura erro se utilizador digitar letras em vez de números
    except ValueError:
        print("Erro nos dados.")


# ----------------------------
# VENDER PRODUTO
# ----------------------------
def vender_produto():
    try:
        # Pede ID do produto e quantidade
        id_prod = int(input("ID do produto: "))
        quantidade = int(input("Quantidade: "))

        # Verifica se quantidade é válida
        if quantidade <= 0:
            print("Quantidade inválida.")
            return

        # Percorre produtos procurando pelo ID
        for i, p in enumerate(produtos):
            if p[0] == id_prod:

                # Verifica se há stock suficiente
                if p[4] >= quantidade:
                    novo_stock = p[4] - quantidade

                    # Atualiza o produto na lista
                    produtos[i] = (p[0], p[1], p[2], p[3], novo_stock)

                    print("Venda realizada com sucesso!")

                    # Aviso caso fique sem stock
                    if novo_stock == 0:
                        print("⚠ Produto esgotado!")
                else:
                    print("Stock insuficiente.")
                return

        # Caso não encontre o produto
        print("Produto não encontrado.")

    except ValueError:
        print("Dados inválidos.")


# ----------------------------
# ADICIONAR AO CARRINHO
# ----------------------------
def adicionar_ao_carrinho(utilizador):
    try:
        # Pede ID do produto
        id_prod = int(input("ID do produto: "))

        # Verifica se já está no carrinho
        if any(item[0] == id_prod for item in utilizador["carrinho"]):
            print("Produto já está no carrinho.")
            return

        # Procura produto na lista geral
        for p in produtos:
            if p[0] == id_prod:

                # Verifica se tem stock
                if p[4] > 0:
                    utilizador["carrinho"].append(p)
                    print("Produto adicionado ao carrinho.")
                else:
                    print("Produto sem stock.")
                return

        print("Produto não encontrado.")

    except ValueError:
        print("ID inválido.")


# ----------------------------
# REMOVER DO CARRINHO
# ----------------------------
def remover_do_carrinho(utilizador):
    # Verifica se carrinho está vazio
    if not utilizador["carrinho"]:
        print("Carrinho vazio.")
        return

    try:
        id_prod = int(input("ID do produto a remover: "))

        # Procura o item dentro do carrinho
        for item in utilizador["carrinho"]:
            if item[0] == id_prod:
                utilizador["carrinho"].remove(item)
                print(f"{item[1]} removido do carrinho.")
                return

        print("Produto não está no carrinho.")

    except ValueError:
        print("ID inválido.")


# ----------------------------
# VER CARRINHO
# ----------------------------
def ver_carrinho(utilizador):
    # Verifica se está vazio
    if not utilizador["carrinho"]:
        print("Carrinho vazio.")
        return

    # Soma total dos preços
    total = sum(item[3] for item in utilizador["carrinho"])

    print("\n=== CARRINHO ===")

    # Mostra cada item
    for item in utilizador["carrinho"]:
        print(f"{item[1]} - {item[3]:.2f}€")

    print(f"Total: {total:.2f}€")


# ----------------------------
# FINALIZAR COMPRA
# ----------------------------
def finalizar_compra(utilizador):
    # Calcula total da compra
    total = sum(item[3] for item in utilizador["carrinho"])

    if total == 0:
        print("Carrinho vazio.")
        return

    # Verifica saldo suficiente
    if utilizador["saldo"] < total:
        print("Saldo insuficiente.")
        return

    # Confirmação do utilizador
    confirmar = input("Confirmar compra? (s/n): ")
    if confirmar.lower() != "s":
        print("Compra cancelada.")
        return

    # Desconta saldo
    utilizador["saldo"] -= total

    # Atualiza stock dos produtos comprados
    for item in utilizador["carrinho"]:
        for i, p in enumerate(produtos):
            if p[0] == item[0] and p[4] > 0:
                novo_stock = p[4] - 1
                produtos[i] = (p[0], p[1], p[2], p[3], novo_stock)

                if novo_stock == 0:
                    print(f"⚠ {p[1]} esgotado!")

    # Guarda no histórico data e total
    utilizador.setdefault("historico", []).append({
        "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "total": total
    })

    # Limpa carrinho
    utilizador["carrinho"].clear()

    print("Compra concluída com sucesso!")


# ----------------------------
# VER DADOS DA CONTA
# ----------------------------
def ver_dados_conta(utilizador):
    print("\n=== DADOS DA CONTA ===")
    print(f"Nome: {utilizador['nome']}")
    print(f"Saldo: {utilizador['saldo']:.2f}€")
    print(f"Itens no carrinho: {len(utilizador['carrinho'])}")
    print(f"Total de compras realizadas: {len(utilizador.get('historico', []))}")


# ----------------------------
# VER HISTÓRICO
# ----------------------------
def ver_historico(utilizador):
    # Obtém histórico (ou lista vazia se não existir)
    historico = utilizador.get("historico", [])

    if not historico:
        print("Nenhuma compra realizada.")
        return

    print("\n=== HISTÓRICO DE COMPRAS ===")

    # Mostra cada compra registrada
    for compra in historico:
        print(f"{compra['data']} - Total: {compra['total']:.2f}€")


# ----------------------------
# VALOR TOTAL DA LOJA
# ----------------------------
def valor_total():
    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    # Valor total = preço × stock
    total = sum(p[3] * p[4] for p in produtos)
    total_unidades = sum(p[4] for p in produtos)

    print("\n=== VALOR TOTAL DA LOJA ===")
    print(f"Total de unidades: {total_unidades}")
    print(f"Valor total em stock: {total:.2f}€")


# ----------------------------
# ALERTA STOCK BAIXO
# ----------------------------
def alerta_stock_baixo():
    encontrou = False

    print("\n=== STOCK BAIXO (<=3) ===")

    # Mostra produtos com stock menor ou igual a 3
    for p in produtos:
        if p[4] <= 3:
            print(f"{p[1]} - Stock: {p[4]}")
            encontrou = True

    if not encontrou:
        print("Nenhum produto com stock baixo.")


# ----------------------------
# PRODUTO DESTAQUE
# ----------------------------
def produto_destaque():
    # Filtra apenas produtos disponíveis
    disponiveis = [p for p in produtos if p[4] > 0]

    if not disponiveis:
        print("Sem produtos disponíveis.")
        return

    # Produto mais caro e mais barato
    mais_caro = max(disponiveis, key=lambda p: p[3])
    mais_barato = min(disponiveis, key=lambda p: p[3])

    print(f"Mais caro: {mais_caro[1]} - {mais_caro[3]:.2f}€")
    print(f"Mais barato: {mais_barato[1]} - {mais_barato[3]:.2f}€")


# ----------------------------
# VER HORA
# ----------------------------
def ver_hora():
    # Mostra data e hora atual formatada
    agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print(f"Hora atual: {agora}")


# ----------------------------
# HORÁRIO FUNCIONÁRIO
# ----------------------------
def horario_funcionario():
    # Mostra horário fixo de trabalho
    print("Horário de trabalho: 09:00 às 18:00")