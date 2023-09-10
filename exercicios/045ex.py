from random import randint
numero_usuario = int(input('''Vamos jogar jokenpô, escolha um número de acordo com as opções abaixo:
[1] PEDRA;
[2] PAPEL;
[3] TESOURA
'''))
numero_pc = randint(1,3)

if numero_usuario == 1 and numero_pc == 2:
    print("Você perdeu!")
