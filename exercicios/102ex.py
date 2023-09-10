def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número
    :param n: O número a ser calculado
    :param show: A opcão para escolher mostrar o cálculo ou não
    :return: O valor do fatorial do número n
    """
    if show == True:
        print(n, end='')
        cont = n
        for i in range(n):
            print(f' x {cont-1}', end='')
            cont -= 1
        print(' = ', end='')
    cont = n
    while cont > 1:
        cont -= 1
        n *= cont
    return n

# programa principal
print(fatorial(5, True))
help(fatorial)