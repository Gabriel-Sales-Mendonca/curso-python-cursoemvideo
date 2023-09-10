sexo = str(input('Digite seu sexo, digite M para masculino e F para feminino: ')).upper().strip()[0]

while sexo != 'M' and sexo != 'F':
    print('Digite um valor válido')
    sexo = str(input('Digite seu sexo, digite M para masculino e F para feminino: ')).upper().strip()[0]
if sexo == 'M':
    print('Seu sexo é masculino')
else:
    print('Seu sexo é feminino')
