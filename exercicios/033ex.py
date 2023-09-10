numero_1 = float(input("Digite um número: "))
numero_2 = float(input("Digite outro número: "))
numero_3 = float(input("Digite o último número: "))

menor = numero_1
maior = numero_1
if numero_2 < numero_1 and numero_2 < numero_3:
    menor = numero_2
if numero_3 < numero_1 and numero_3 < numero_2:
    menor = numero_3
if numero_2 > numero_1 and numero_2 > numero_3:
    maior = numero_2
if numero_3 > numero_1 and numero_3 > numero_2:
    maior = numero_3
print(f"O maior número é 0 {maior} e o menor número é o {menor}")
