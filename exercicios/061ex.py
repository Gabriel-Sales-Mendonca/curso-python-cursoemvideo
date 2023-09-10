primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))
c = 0
while c < 10:
    print(primeiro_termo, end='')
    if c < 9:
        print('-', end='')
    primeiro_termo += razao
    c += 1
print(' ACABOU !')
