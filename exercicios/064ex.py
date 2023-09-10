num = 0
c = -1
soma = 0
while num != 999:
    num = int(input('Digite um número e quando quiser parar digite o número 999: '))
    c += 1
    if num != 999:
        soma += num
print(f'Você digitou {c} números e a soma entre eles é {soma}.')
