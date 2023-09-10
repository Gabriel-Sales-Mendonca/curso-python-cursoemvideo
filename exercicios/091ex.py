from random import randint
from operator import itemgetter
from time import sleep

jogadores = dict()
lista_jogadores = []

jogadores['jogador1'] = randint(1, 6)
jogadores['jogador2'] = randint(1, 6)
jogadores['jogador3'] = randint(1, 6)
jogadores['jogador4'] = randint(1, 6)

for chave, valor in jogadores.items():
    print(f'{chave} tirou {valor} no dado')
    sleep(1)

print('-----RANKING-----')

lista_jogadores = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

for i, valor in enumerate(lista_jogadores):
    print(f'{i+1}º {valor[0]}: {valor[1]}')
    sleep(1)