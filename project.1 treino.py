print("==========================================")
print("        SISTEMA DE SEGURANÇA")
print("     Geração de Siglas e Passwords")
print("==========================================")

# -------------------------------------------------
# FUNÇÃO: MOSTRAR MENU
# -------------------------------------------------

def mostrar_menu():
    print("\n============== MENU ==============")
    print("1 - Gerar SIGLA")
    print("2 - Gerar PASSWORD")
    print("3 - Ver última password")
    print("4 - Ver força da password")
    print("5 - Ver regras de segurança")
    print("6 - Ajuda")
    print("7 - Sair")
    print("==================================")

# -------------------------------------------------
# FUNÇÃO: GERAR SIGLA
# -------------------------------------------------
def gerar_sigla(nome):
    palavras = nome.split()
    sigla = ""

    for palavra in palavras:
        if len(palavra) >= 2:
            sigla += palavra[0].upper()
            sigla += palavra[1].lower()
        else:
            sigla += palavra[0].upper()

    sigla += str(len(palavras))
    sigla += "!"

    return sigla

# -------------------------------------------------
# FUNÇÃO: GERAR PASSWORD (simples mas forte)
# -------------------------------------------------
def gerar_password(resposta):
    texto = resposta.replace(" ", "")
    password = ""

    for letra in texto:
        if letra.lower() in "aeiou":
            password += letra.upper()
        else:
            password += letra.lower()

    password += str(len(texto))
    password += "#"

    return password

# -------------------------------------------------
# FUNÇÃO: VERIFICAR FORÇA DA PASSWORD
# -------------------------------------------------
def verificar_forca(password):
    tem_maiuscula = False
    tem_minuscula = False
    tem_numero = False
    tem_simbolo = False

    for c in password:
        if c.isupper():
            tem_maiuscula = True
        elif c.islower():
            tem_minuscula = True
        elif c.isdigit():
            tem_numero = True
        else:
            tem_simbolo = True

    tamanho = len(password)

    if tamanho >= 10 and tem_maiuscula and tem_minuscula and tem_numero and tem_simbolo:
        return "FORTE"
    elif tamanho >= 8:
        return "MÉDIA"
    else:
        return "FRACA"

# -------------------------------------------------
# PROGRAMA PRINCIPAL
# -------------------------------------------------
def main():
    ultima_password = ""
    ultima_forca = ""

    print("\nBem-vindo ao sistema de segurança")

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        # OPÇÃO 1 - SIGLA
        if opcao == "1":
            nome = input("Digite o nome completo: ")

            if nome == "":
                print("Nome inválido.")
            else:
                sigla = gerar_sigla(nome)
                print("Sigla gerada:", sigla)

        # OPÇÃO 2 - PASSWORD
        elif opcao == "2":
            pergunta = input("Qual sua série favorita? ")

            if pergunta == "":
                print("Resposta inválida.")
            else:
                password = gerar_password(pergunta)
                forca = verificar_forca(password)

                ultima_password = password
                ultima_forca = forca

                print("Password gerada:", password)
                print("Força:", forca)

        # OPÇÃO 3 - ÚLTIMA PASSWORD
        elif opcao == "3":
            if ultima_password == "":
                print("Nenhuma password gerada ainda.")
            else:
                print("Última password:", ultima_password)

        # OPÇÃO 4 - FORÇA
        elif opcao == "4":
            if ultima_password == "":
                print("Nenhuma password disponível.")
            else:
                print("Força da password:", ultima_forca)

        # OPÇÃO 5 - REGRAS
        elif opcao == "5":
            print("\nREGRAS DE SEGURANÇA")
            print("- Não usar apenas letras")
            print("- Usar números e símbolos")
            print("- Password com bom tamanho")
            print("- Não partilhar passwords")

        # OPÇÃO 6 - AJUDA
        elif opcao == "6":
            print("\nAJUDA")
            print("1 - Gera sigla a partir do nome")
            print("2 - Gera password a partir da série")
            print("3 - Mostra a última password")
            print("4 - Mostra a força da password")

        # OPÇÃO 7 - SAIR
        elif opcao == "7":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida.")

# -------------------------------------------------
# EXECUÇÃO
# -------------------------------------------------
if __name__ == "__main__":
    main()
