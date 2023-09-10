matriz = [[], [], [], [], [], [], [], [], []]

n = 0
for c in range(9):
    if c < 4:
        valor = int(input(f'Digite um valor para [0, {n}]: '))
        matriz[c].append(valor)
    elif 3 < c < 7:
        valor = int(input(f'Digite um valor para [1, {n}]: '))
        matriz[c].append(valor)
    else:
        valor = int(input(f'Digite um valor para [2, {n}]: '))
        matriz[c].append(valor)
    n += 1
    if n == 3 or n == 6:
        n = 0
print(f'{matriz[0]} {matriz[1]} {matriz[2]}')
print(f'{matriz[3]} {matriz[4]} {matriz[5]}')
print(f'{matriz[6]} {matriz[7]} {matriz[8]}')
