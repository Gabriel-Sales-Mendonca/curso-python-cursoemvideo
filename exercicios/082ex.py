lista_todos = []
lista_par = []
lista_impar = []
qtd = 1
while True:
    lista_todos.append(int(input(f'Digite o {qtd}º número: ')))
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar [S/N] ? ')).upper().strip()[0]
    if resp in 'N':
        break
    qtd += 1
for n in range(0, len(lista_todos)):
    if lista_todos[n] % 2 == 0:
        lista_par.append(lista_todos[n])
    else:
        lista_impar.insert(-1, lista_todos[n])
print(f'Números digitados: {lista_todos}')
print(f'Números pares: {lista_par}')
print(f'Números ímpares: {lista_impar}')
