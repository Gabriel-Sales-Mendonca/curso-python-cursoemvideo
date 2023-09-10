#calcula a área do terreno
def area(l, c):
    area = l * c
    print(f'A área do terreno é {area}m²')

#mostra o título formatado
def titulo():
    print('-'*50)
    print('Cálculo da Área de um terreno'.center(50))
    print('-'*50)


titulo()

while True:
    try:
        area(float(input('Informe a largura do terreno: ')), float(input('Informe o comprimento do terreno: ')))
        break #caso o usuario digite numeros o loopi se encerra
    except ValueError:
        print('Valor inválido. Informe um número')