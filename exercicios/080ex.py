numero = []
for c in range(0, 4):
    valor = int(input('Digite um número: '))
    if c == 0 or valor > numero[-1]:
        numero.append(valor)
    else:
        pos = 0
        while pos < len(numero):
            if valor <= numero[pos]:
                numero.insert(pos, valor)
                break
            pos += 1
print(numero)
