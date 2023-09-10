cont_idade = cont_homem = cont_mulher = 0
while True:
    print('_'*30)
    print('CADASTRE UMA PESSOA')
    print('_'*30)
    idade = int(input('Idade: '))
    if idade >= 18:
        cont_idade += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    if sexo in 'M':
        cont_homem += 1
    elif sexo in 'F' and idade < 20:
        cont_mulher += 1
    print('_'*30)
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if opcao == 'N':
        break
print('FIM DO PROGRAMA')
print(f'''Total de pessoas com mais de 18 anos: {cont_idade}
Ao todo temos {cont_homem} homens cadastrados
E temos {cont_mulher} mulheres com menos de 20 anos''')
