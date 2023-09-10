numeros = []
while True:
    numero = int(input('Digite um número: '))
    numeros.append(numero)
    opcao = 'e'
    while opcao not in 'SN':
        opcao = str(input('Deseja digitar outro número[S/N]: ')).upper().strip()[0]
    if opcao == 'N':
        break
print(f'Foram digitados {len(numeros)} números.')
numeros.sort(reverse=True)
print(f'Números digitados em ordem decrescente: {numeros}')
if 5 in numeros:
    print('O número 5 está na lista')
else:
    print('Você não digitou o número 5')
