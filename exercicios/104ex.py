def leiaInt(n):
    while True:
        numeroLocal = input(n)
        if numeroLocal.isnumeric():
            return int(numeroLocal)
        else:
            print('ERRO!',end=' ')
            

#programa principal
numero = leiaInt('Digite um número inteiro: ')
print(f'O número digitado foi {numero}.')