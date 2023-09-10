# Esse código tem a função de embaralhar os nomes dos alunos e gerar uma ordem aleatória
from random import shuffle

print('Digite o nome dos alunos em sequência:')
a1 = input('Priemiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
lista = [a1, a2, a3, a4]
shuffle(lista)

print('a ordem dos alunos será')
print(lista)
