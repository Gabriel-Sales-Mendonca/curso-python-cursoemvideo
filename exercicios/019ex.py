from random import choice

print('Insira em sequência os nomes dos alunos:')

a1 = input('1: ')
a2 = input('2: ')
a3 = input('3: ')
a4 = input('4: ')

alunos = [a1, a2, a3, a4]

sorteado = choice(alunos)

print('O aluno sorteado foi o {}!'.format(sorteado))
