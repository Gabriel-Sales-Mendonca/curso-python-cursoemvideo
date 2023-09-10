lista_dicionarios = list()

cont = 0
resp = 'S'
while resp == 'S':
    pessoa = dict()
    pessoa['nome'] = str(input('Nome: ')).strip()
    pessoa['sexo'] = str(input('Sexo: ')).strip().upper()[0]
    pessoa['idade'] = int(input('Idade: '))
    lista_dicionarios.append(pessoa)
    cont += 1
    resp = str(input('Quer continuar [S/N]: ')).upper().strip()[0]

soma = 0
for c in lista_dicionarios:
    soma += c['idade']
media = soma / len(lista_dicionarios)

print(f'Foram cadastradas {cont} pessoa(s).')
print(f'A média das idades cadastradas é de {media}')

lista_mulheres = []
for i in lista_dicionarios:
    if i['sexo'] == 'F':
        lista_mulheres.append(i['nome'])
print(f'A lista de mulheres cadastradas é {lista_mulheres}')

pessoas_idade_acima_media = []
for i in lista_dicionarios:
    if i['idade'] > media:
        pessoas_idade_acima_media.append(i['nome'])
print(f'Lista de pessoas com idade acima da média: {pessoas_idade_acima_media}')