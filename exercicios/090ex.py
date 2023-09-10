alunos = {}
alunos['nome'] = str(input('Nome: '))
alunos['media'] = float(input('Média: '))
if alunos['media'] >= 7:
    alunos['situacao'] = 'APROVADO'
else:
    alunos['situacao'] = 'REPROVADO'
for k, v in alunos.items():
    print(f'{k} é igual a {v}')
