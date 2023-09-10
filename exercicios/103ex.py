def ficha(nome='desconhecido', gols=0):
    print(f'O jogador {nome} marcou {gols} gol(s)')


nome = str(input('Nome do jogador: ')).strip()
gols = input('Número de gols: ')

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

# caso a variavel nome seja uma string vazia a função ficha será chamada somente com o parâmetro gols
if nome == '':
    ficha(gols=gols)
else:
    ficha(nome, gols)