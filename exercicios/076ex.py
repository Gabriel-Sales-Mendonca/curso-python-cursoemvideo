listagem = ('Lápis', 2,
            'Borracha', 1.9,
            'Caderno', 6.59,
            'Caneta', 3)
print('-'*40)
print(f'{"Listagem de Preços":^40}')
print('-'*40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R$ {listagem[pos]:.2f}')
print('-'*40)
