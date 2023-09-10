import random
from time import sleep
num = int(input('Digite um número inteiro entre 0 e 5: '))
opcoes = [1, 2, 3, 4]
sorteado = random.choice(opcoes)
print("PROCESSANDO...")
sleep(2)
if sorteado == num:
    print('Parabéns, você acertou o número sorteado!')
else:
    print('Você não acertou o número sorteado, tente novamente!')
