saque = int(input('Qual o valor a ser sacado ? (número inteiro) '))
cont_cinquenta = cont_vinte = cont_dez = cont_um = 0
while saque >= 50:
    cont_cinquenta += 1
    saque -= 50
while saque >= 20:
    cont_vinte += 1
    saque -= 20
while saque >= 10:
    cont_dez += 1
    saque -= 10
while saque >= 1:
    cont_um += 1
    saque -= 1
print(f'{cont_cinquenta} notas de R$50,00.')
print(f'{cont_vinte} notas de R$20,00.')
print(f'{cont_dez} notas de R$10,00.')
print(f'{cont_um} notas de R$1,00')
