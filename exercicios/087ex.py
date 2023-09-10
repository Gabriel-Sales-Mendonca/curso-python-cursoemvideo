matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for c in range(3):
    for x in range(3):
        valor = int(input(f'Digite um valor para [{c}, {x}]: '))
        matriz[c][x] = valor

for c in range(3):
    for x in range(3):
        print(f'[{matriz[c][x]:^5}]', end=' ')
    print()

somaPar = 0
somaTerceiraColuna = 0

for c in range(3):
    for x in range(3):
        if x == 2:
            terceiraColuna = matriz[c][2]
            somaTerceiraColuna += terceiraColuna
        if matriz[c][x] % 2 == 0:
            par = matriz[c][x]
            somaPar += par
matriz[1].sort()

print(f'A soma de todos os valores pares digitados é {somaPar}')
print(f'A soma dos valores da terceira coluna é {somaTerceiraColuna}')
print(f'O maior valor da segunda linha é o {matriz[1][2]}')
