'''num_inicial = int(input('Digite um número: '))
num = num_inicial

if num_inicial < 0:
    print('O número deve ser maior ou igual a zero')
elif num_inicial == 0:
    print('O fatorial de 0 é 1')
else:
    resultado = 1
    while num != 1:
        resultado = resultado * num
        num -= 1

    print(f'O fatorial do número {num_inicial} é {resultado}')'''

num_inicial = int(input('Digite um número: '))
num = num_inicial

if num < 0:
    print('O número deve ser maior ou igual a zero')
elif num == 0:
    print('O fatorial de 0 é 1')
else:
    resultado = 1
    while num > 0:
        print(f'{num}', end='')
        if num > 1:
            print(' X ', end='')
        resultado = resultado * num
        num -= 1
    print(f' = {resultado}')
