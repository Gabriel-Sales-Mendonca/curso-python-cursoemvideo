while True:
    try:
        num = (int(input('Digite um número: ')),
               int(input('Digite outro número: ')),
               int(input('Digite outro número: ')),
               int(input('Digite o útlimo número: ')))
        break
    except ValueError:
        print('Valor inválido!')
print(f'Os números digitados foram {num}')
print(f'O valor 9 apareceu {num.count(9)} vez(es).')
try:
    print(f'O primeiro valor 3 foi digitado na {num.index(3)+1}ª posição.')
except ValueError:
    print('O número 3 não foi digitado nenhuma vez.')
print('Os valores pares digitados foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
