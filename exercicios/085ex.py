lista = [[], []]

contaPrimeiroPar = contaPrimeiroImpar = 0
contador = 1
for c in range(1, 8):
    valor = int(input(f'Digite o {contador}º valor: '))
    if contador == 1:
        if valor % 2 == 0:
            lista[0].append(valor)
            contaPrimeiroPar += 1
        else:
            lista[1].append(valor)
            contaPrimeiroImpar += 1

        # Adicionando na ordem o valor digitado na sublista de valores pares
    else:
        if valor % 2 == 0:
            n = 0
            comprimento = len(lista[0])
            while n < comprimento:
                if valor <= lista[0][n]:
                    lista[0].insert(n, valor)
                    break
                n += 1
            if contaPrimeiroPar == 0:
                lista[0].append(valor)
                contaPrimeiroPar += 1
            elif contaPrimeiroPar == 1 and valor > lista[0][comprimento - 1]:
                lista[0].append(valor)
                
        # Adicionando na ordem o valor digitado na sublista de valores impares
        else:
            n = 0
            comprimento = len(lista[1])
            while n < comprimento:
                if valor <= lista[1][n]:
                    lista[1].insert(n, valor)
                    break
                n += 1
            if contaPrimeiroImpar == 0:
                lista[1].append(valor)
                contaPrimeiroImpar += 1
            elif contaPrimeiroImpar == 1 and valor > lista[1][comprimento - 1]:
                lista[1].append(valor)
    contador += 1
print(f'Os valores pares digitados em ordem foram {lista[0]}')
print(f'Os valores ímpares digitados em ordem foram {lista[1]}')
