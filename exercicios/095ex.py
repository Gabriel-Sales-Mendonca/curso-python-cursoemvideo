time = []
opcao = 'S'

while opcao == 'S':
    jogador = {
        'nome': str(input('Nome do jogador: ')).strip(),
        'n_partidas': int(input('Quantas partidas ele jogou: '))
    }

    jogador['qtd'] = 0
    for c in range(jogador['n_partidas']):
        jogador[c] = int(input(f'Quantos gols na {c+1}ª partida: '))
        jogador['qtd'] += jogador[c]

    opcao = 'x'
    while opcao not in 'SN':
        opcao = str(input('Quer continuar ? ')).strip().upper()[0]

    time.append(jogador)

print('cod' + ' '*5 + 'nome' + ' '*5 + 'gols' + ' '*5 + 'total')
