primeiro_num = float(input("Digite um número: "))
soma = 0
for c in range(1, 6):
    num = float(input("Digite outro número: "))
    if num % 2 == 0:
        soma += num
if primeiro_num % 2 == 0:
    soma_final = soma + primeiro_num
    print(f"A soma dos números pares que você digitou é igual a {soma_final}")
else:
    print(f"A soma dos números pares que você digitou é igual a {soma}")
