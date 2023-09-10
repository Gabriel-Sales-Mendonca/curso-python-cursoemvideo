from datetime import datetime

pessoa = {'nome': str(input('Nome: ')),
        'nascimento': int(input('Ano de nascimento: ')),
        'ctps': int(input('Carteira de trabalho (caso não tenha digite 0): '))}
if pessoa['ctps'] != 0:
    pessoa['ano_de_contratacao'] = int(input('Ano de contratação: '))
    pessoa['salario'] = round(float(input('Salário: R$')), 2)

data = datetime.now().year
pessoa['aposentadoria'] = 65 - (data - pessoa['nascimento'])

for chave, valor in pessoa.items():
    print(f'    - {chave} tem o valor {valor}')
