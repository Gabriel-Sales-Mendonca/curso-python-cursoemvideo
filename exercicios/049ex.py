from time import sleep
num = int(input("Digite um número inteiro para ver sua tabuada: "))

print("-"*11)
for c in range(1, 11):
    print(f"{num} x {c} = {num * c}")
    sleep(0.5)
print("-"*11)
