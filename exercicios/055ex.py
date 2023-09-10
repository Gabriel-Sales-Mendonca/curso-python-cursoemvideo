'''peso = []
for c in range(1, 6):
    pessoa = float(input("Digite o peso da {}º pessoa:".format(c)))
    peso.append(pessoa)
peso.sort()

maior = peso[-1]
menor = peso[0]

print("O maior peso é o {}".format(maior))
print("O menor peso é o {}".format(menor))'''

maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input("Peso da {}º pessoa: ".format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        else:
            menor = peso
print(maior)
print(menor)
