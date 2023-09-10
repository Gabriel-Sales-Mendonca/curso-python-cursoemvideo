while True:
    num = int(input('Quer ver a tabuada de qual valor ? '))
    if num < 0:
        break
    multiplicador = 1
    print('_'*30)
    while multiplicador <= 10:
        print(f'{num} x {multiplicador} = {num * multiplicador}')
        multiplicador += 1
    print('_'*30)
print('\nACABOU, VOLTE SEMPRE!')
