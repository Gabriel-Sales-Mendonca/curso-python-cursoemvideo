opcao = str(input('Deseja digitar um número ? Digite [s] SIM ou [n] NÃO: ')).upper()
cont = soma = num = menor = maior = 0
while opcao == 'S':
    num = float(input('Digite um número: '))
    soma += num
    if cont == 0:
        menor = num
        maior = num
    elif num < menor:
        menor = num
    elif num > maior:
        maior = num
    opcao = str(input('Deseja digitar um número ? Digite [s] SIM ou [n] NÃO: ')).upper().strip()[0]
    cont += 1
media = soma / cont
print(f'''A média dos valores que você digitou é {media}
O menor número digitado foi {menor}
O maior número digitado foi {maior}''')
