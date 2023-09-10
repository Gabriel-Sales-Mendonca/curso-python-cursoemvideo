num = int(input("Digite um número: "))
divisivel = 0
for c in range(1, num + 1):
    if num % c == 0:
        divisivel += 1
if divisivel == 2:
    print("O número {} é primo".format(num))
else:
    print("O número {} NÃO é primo".format(num))
