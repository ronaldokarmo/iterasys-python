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
            print(f"0{numero + 1} voto - {nome}")
        elif numero < 9:
            print(f"0{numero + 1} votos - {nome}")
        else:
            print(f"{numero + 1} votos - {nome}")

def brinca_plim(fim):
    for numero in range(fim+1):
        if numero % 4 == 0:
            print("PLIM!")
        else:
            #print(f"{numero}")
            print('{:0>3}'.format(numero))

if __name__ == '__main__':
    print_hi("Ronaldo do Carmo.")
    print(f"Rectangle Area: {calcular_area_rectangle(3, 4)} m²")
    print(f"Quadratic Area: {calcular_area_quadratic(5)} m²")
    print(f"Triangle Area: {calcular_area_triangle(6, 7)} m²")
    contar_progressivamente(10)
    apoiar_canditado("Paulo Nobre", 99)
    brinca_plim(100)
