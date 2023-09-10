while True:
    valores = []
    c = 1
    while c < 3:
        num = float(input('{}º número: '.format(c)))
        valores.append(num)
        c += 1

    print('''
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA''')

    operacao = int(input('Digite um número correspondente a operação que deseja realizar: '))

    if operacao == 1:
        print('A soma entre os valores digitados é de {}'.format(valores[0] + valores[1]))
    elif operacao == 2:
        print('A multiplicação entre os números digitados é de {}'.format(valores[0] * valores[1]))
    elif operacao == 3:
        valores.sort()
        print('O maior valor digitado foi o {}'.format(valores[1]))
    elif operacao == 4:
        print('Digite novos números:')
        continue
    break
