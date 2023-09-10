from random import randint
cont = 0
while True:
    opcao = ' '
    while opcao not in 'PI':
        opcao = str(input('[P]PAR ou [I]ÍMPAR: ')).upper().strip()[0]
    num_pessoa = int(input('Escolha um número inteiro entre 0 e 5: '))
    num_pc = randint(0, 5)
    soma = num_pessoa + num_pc
    if soma % 2 == 0 and opcao == 'P':
        print(f'PARABÉNS VOCÊ GANHOU! O computador escolheu o número {num_pc} e você o número {num_pessoa}, total deu {soma} que é PAR')
        cont += 1
    elif soma % 2 != 0 and opcao =='I':
        print(f'PARABÉNS VOCÊ GANHOU!O computador escolheu o número {num_pc} e você o número {num_pessoa}, total deu {soma} que é ÍMPAR')
        cont += 1
    else:
        print(f'VOCÊ PERDEU! O computador escolheu o número {num_pc} e você o número {num_pessoa}, total deu {soma}')
        break
print(f'Você conseguiu {cont} vitórias consecutivas!')
