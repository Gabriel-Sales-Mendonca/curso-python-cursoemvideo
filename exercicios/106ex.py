def manual(funcao):
    '''
    -> Essa função tem o objetivo de retornar a docstring de alguma função ou biblioteca em python
    param: funcao: recebe o nome da função ou biblioteca
    return: retorna a docstring da função ou biblioteca
    '''
    return help(funcao)


while True:
    print('~'*30)
    print('SISTEMA DE AJUDA pyHELP'.center(28))
    print('~'*30)
    comando = str(input('função ou biblioteca > ')).strip()

    manual(comando)

    while True:
        resp = str(input('Quer continuar ? Digite SIM ou NÃO: ')).strip().upper()[0]
        
        if resp in 'SN':
            break
    if resp == 'N':
        break