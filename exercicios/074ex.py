from random import randint
num = (randint(0, 5), randint(0, 5), randint(0, 5), randint(0, 5), randint(0, 5))
print('Lista de números gerados: ', end='')
for n in num:
    print(f'{n}', end=',')
print(f'\nO MENOR valor da lista é o {max(num)}')
print(f'O MAIOR valor da lista é o {min(num)}')
