valores = []
for c in range(5):
    if c == 0:
        valores.append(float(input('Digite um número: ')))
    elif 0 < c < 4:
        valores.append(float(input('Digite outro número: ')))
    else:
        valores.append(float(input('Digite o último número: ')))

maior = max(valores)
menor = min(valores)
pos_maior = valores.index(maior)
pos_menor = valores.index(menor)

print(f'O maior valor digitado foi o {maior} na posição {pos_maior+1}')
print(f'O menor valor digitado foi o {menor} na posição {pos_menor+1}')
