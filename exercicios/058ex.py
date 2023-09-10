import random

opcoes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num_pc = random.choice(opcoes)

print('-'*60)
num = int(input('''O PC pensou em um número, tente adivinhar em qual número foi.
Escolha um número entre 0 e 10: '''))
print('-'*60)

contador = 1

while num != num_pc:
    num = int(input('Você errou, tente novamente: '))
    contador += 1
print('Parabéns, você ACERTOU, o PC pensou no número {}, e você precisou de {} palpite(s)'.format(num_pc, contador))
