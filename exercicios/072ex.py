num_ext = ('Zero', 'Um', 'Dois', 'Três', 'Quatro',
           'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
           'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze',
           'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
opcao = 'S'
while opcao == 'S':
    while True:
        try:
            num = int(input('Digite um número entre 0 e 20: '))
            if 0 <= num <= 20:
                print(f'O número digitado por extenso é: {num_ext[num]}')
                break
            else:
                print('Número inválido, tente um número entre 0 e 20.')
        except ValueError:
            print('Valor digitado inválido, Digite um número ao invés de escreve-lo por extenso!')
    while True:
        opcao = str(input('Você quer continuar ? (S / N): ')).upper().strip()[0]
        if opcao in 'SN':
            break
        print('Letra inválida')
