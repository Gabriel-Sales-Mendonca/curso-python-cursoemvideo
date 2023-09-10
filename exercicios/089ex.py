notas = []
nota_aluno = []
opcao = 'S'

while opcao == 'S':
    nome = str(input('Digite o nome do aluno: '))
    nota_aluno.append(nome)
   
    for c in range(2):
        nota = float(input(f'Digite a {c+1}º nota: '))
        nota_aluno.append(nota)
   
    media = (nota_aluno[1] + nota_aluno[2]) / 2
    nota_aluno.append(media)
       
    notas.append(nota_aluno[:])
    nota_aluno.clear()
   
    opcao = 'x'
    while opcao not in 'SN':
        opcao = str(input('Quer continuar [S/N]? ')).upper().strip()[0]
        if opcao == 'N':
            break
   
    if opcao == 'N':
        break
   
print('-----BOLETIM-----')
print()
for n in range(0, len(notas)):
    print(f'Nome: {notas[n][0]}')
    print(f'Média: {notas[n][3]}')
    print()