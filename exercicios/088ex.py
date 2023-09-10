from random import randint
from time import sleep

print('-'*30)
print('JOGO DA MEGA SENA')
print('-'*30)

lista_jogos = []

n_jogos = int(input('Quantos jogos você quer que eu sorteie ? '))

print(f'Sorteando {n_jogos} jogos')

for n in range(n_jogos):
    for c in range(6):
        jogo = randint(1, 60)
        lista_jogos.append(jogo)
    sleep(1)
    print(f'Jogo {n + 1}: {lista_jogos}')
    lista_jogos.clear()
