num = int(input('Digite um número inteiro: '))
c = 0
numf_ant = 0
numf_atual = 1
soma = 0

while c < num - 1:
    soma = numf_ant + numf_atual
    numf_ant = numf_atual
    numf_atual = soma
    if c == 0:
        print('0', end='-')
    c += 1
    print(f'{soma}', end='-')
print('Fim')
