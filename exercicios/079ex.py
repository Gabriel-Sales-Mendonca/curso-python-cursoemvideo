valores = []
while True:
    while True:
        try:
            num = (float(input('Digite um valor: ')))
            break
        except ValueError:
            print('Valor inválido!')
    if num not in valores:
        valores.append(num)
        print('Valor adicionado com sucesso...')
    elif num in valores:
        print('Esse valor já foi adicionado com sucesso...')
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar[S/N] ? ')).upper().strip()[0]
    if opcao == 'N':
        break
valores.sort()
print(valores)
