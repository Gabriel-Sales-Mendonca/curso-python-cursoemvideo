def leiaInt(n):
    while True:
        try:
            numeroLocal = int(input(n))
            return numeroLocal
        except ValueError:
            print('\033[31mERRO com o tipo de dado inserido! Por favor digite um número inteiro\033[m')
        else:
            break


def leiaFloat(n):
    while True:
        try:
            numeroRealLocal = float(input(n))
            numero = f'{numeroRealLocal}'.replace('.',',')
            return numero
        except ValueError:
            print('\033[31mERRO com o tipo de dado inserido! Por favor digite um número inteiro\033[m')
        else:
            break


#programa principal
numero = leiaInt('Digite um número inteiro: ')
numeroReal = leiaFloat('Digite um número real: ')

print(f'Os número digitado foram {numero} e {numeroReal}.')