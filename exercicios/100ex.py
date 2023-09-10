from random import randint

numeros = []
def sorteia():
    for c in range(5):
        valor = randint(1, 100)
        numeros.append(valor)
    print('Os números sorteados foram ', end='')
    for num in numeros:
        print(f'{num}', end=' ')

pares = []
def somaPar():
    for v in numeros:
        if v % 2 == 0:
            pares.append(v)
    print(f'\nA soma entre todos os números pares sorteados foi {sum(pares)}')


sorteia()
somaPar()
