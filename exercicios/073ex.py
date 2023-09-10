times = ('Cruzeiro', 'Vasco', 'Flamengo', 'Palmeiras', 'Botafogo', 'Corinthias',
         'Atlético-MG', 'América', 'Internacional', 'Chapecoense', 'Bahia', 'Ceará',
         'Ponte Preta', 'Vila Nova', 'Santos', 'Fluminense', 'Grêmio', 'São Paulo', 'Fortaleza', 'Coritiba')
print('-'*100)
print(f'Os 20 primeiros colocados da tabela são: {times}')
print('-'*100)
print(f'Os 5 primeiros times da tabela são: {times[:5]}.')
print('-'*100)
print(f'Os 4 últimos colocados da tabela são: {times[-4:]}.')
print('-'*100)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-'*100)
print(f'A Chapecoense está na {times.index("Chapecoense")+1}ª posição da tabela.')
