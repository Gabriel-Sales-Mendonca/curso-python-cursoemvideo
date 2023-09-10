titulo = 'SOMANDO VALORES'
print(f'{titulo:-^35}')

cont = soma = 0
while True:
    num = int(input('Digite um número (999 para parar): '))
    if num == 999:
        break
    soma += num
    cont += 1
print(f'A soma dos {cont} valores digitados é {soma}')
