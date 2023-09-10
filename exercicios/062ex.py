primeiro_termo = int(input('Digite o primeiro termo: '))
termo = primeiro_termo
razao = int(input('Digite a razao: '))
c = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while c <= total:
        print(f'{termo} -', end='')
        termo += razao
        c += 1
    print(' PAUSA !')
    mais = int(input('Quantos termos deseja adicionar ? '))
print('ACABOU')
