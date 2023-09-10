from time import sleep

def contagem(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    elif passo == 0:
        passo = 1
    print('~'*40)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if inicio < fim:
        while True:
            print(inicio,end=' ', flush=True) # o flush eh necessario para forçar a liberacao do buffer
            inicio += passo
            sleep(0.5)
            if inicio > fim:
                print('FIM!')
                break
    else:
        while True:
            print(inicio,end=' ', flush=True) # o flush eh necessario para forçar a liberacao do buffer
            inicio -= passo
            sleep(0.5)
            if inicio < fim:
                print('FIM!')
                break
    print('~'*40)

contagem(1, 10, 1)
contagem(10, 0, 2)
print('Agora é sua hora de personalizar a contagem!')

while True:
    try:
        contagem(int(input('Inicio: ')), int(input('Fim: ')), int(input('Passo: ')))
    except ValueError:
        print('Valor inválido, digite os valores novamente!')
        break
    break