print('-'*30)
print('LOJA')
print('-'*30)

preco = cont = mil = preco_barato = soma = 0
barato = ' '
while True:
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    if preco > 1000:
        mil += 1
    if cont == 0 or preco < preco_barato:
        preco_barato = preco
        barato = nome
    soma += preco
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar ? [S/N] ')).upper().strip()[0]
    if opcao == 'N':
        break
    cont += 1

print('{:-^30}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi R${soma:.2f}')
print(f'Temos {mil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${preco_barato:.2f}')
