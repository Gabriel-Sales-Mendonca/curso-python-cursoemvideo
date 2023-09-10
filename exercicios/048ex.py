contador = 0
soma = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma = soma + c
        contador = contador + 1
print(f"A soma dos {contador} números que são múltiplos de 3 é igual a {soma}.")
