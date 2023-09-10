jogador = {
    'nome': str(input('Nome do jogador: ')).strip(),
    'n_partidas': int(input('Quantas partidas ele jogou: '))
}

jogador['qtd'] = 0
for c in range(jogador['n_partidas']):
    jogador[c] = int(input(f'Quantos gols na {c+1}ª partida: '))
    jogador['qtd'] += jogador[c]

print(f'\nO jogador {jogador["nome"]} jogou {jogador["n_partidas"]} partidas.\n')
for i in range(jogador['n_partidas']):
    print(f'marcou {jogador[i]} gol(s) na {i+1}ª partida.')
print(f'\nE marcou {jogador["qtd"]} gol(s) no total.')
