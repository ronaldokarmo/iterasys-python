def print_hi(name):
    print(f'Hi, {name}')


def calcular_area_rectangle(largura, comprimento):
    return largura * comprimento


def calcular_area_quadratic(lado):
    return lado ** 2


def calcular_area_triangle(largura, comprimento):
    return largura * comprimento / 2


def contar_progressivamente(fim):
    for numero in range(fim):
        print(f"Contagem: {numero}")


def apoiar_canditado(nome, qnt):
    for numero in range(qnt):
        if numero < 1:
            print(f"0{numero + 1} voto  - {nome}")
        elif numero < 9:
            print(f"0{numero + 1} votos - {nome}")
        else:
            print(f"{numero + 1} votos - {nome}")


def brinca_plim(fim):
    for numero in range(fim + 1):
        if numero % 4 == 0:
            print("PLIM!")
        else:
            # print(f"{numero}")
            print('{:0>3}'.format(numero))


def exibir_menu():
    print("#########################################################")
    print("##                    MENU DE OPÇÕES                   ##")
    print("#########################################################")
    print("##                                                     ##")
    print("##    1 - Olá, mundo                                   ##")
    print("##    2 - Área do Retangulo                            ##")
    print("##    3 - Área do Quadrado                             ##")
    print("##    4 - Área do Triâgunlo                            ##")
    print("##    5 - Contagem Progressiva                         ##")
    print("##    6 - Contar Votos                                 ##")
    print("##    7 - Brincar de Plim                              ##")
    print("##                                                     ##")
    print("##    0 - Sair                                         ##")
    print("#########################################################")


if __name__ == '__main__':
    menu = "C"
    while menu.upper() != "Z":
        exibir_menu()

        opcao = input("Escolha uma opção conforme o Menu: ")

        if opcao.upper() != "0":
            print(f"\nVocê selecionou a opção do Menu: {opcao}")
            if opcao == "1":
                print_hi("Ronaldo do Carmo.")
            elif opcao == "2":
                print(f"Área do Retangulo: {calcular_area_rectangle(3, 4)} m²")
            elif opcao == "3":
                print(f"Área do Quadrado: {calcular_area_quadratic(5)} m²")
            elif opcao == "4":
                print(f"Área do Triâgunlo: {calcular_area_triangle(6, 7)} m²")
            elif opcao == "5":
                contar_progressivamente(10)
            elif opcao == "6":
                apoiar_canditado("Paulo Nobre", 10)
            elif opcao == "7":
                brinca_plim(16)
            else:
                print("Escolha de Menu Inválido. Selecione uma opção de menu entre 1 a 7!")
        else:
            menu = "Z"
            print(f"\nVocê selecionou a opção Sair.")
            print("Obrigado e volte sempre!")
