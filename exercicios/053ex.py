frase = str(input("Digite uma frase: ")).strip().lower()
junto = "".join(frase.split())
inverso = ""

for i in range(len(junto) - 1, -1, -1):
    inverso = inverso + junto[i]

if junto == inverso:
    print("A frase que você digitou foi {}, e o inverso dessa frase é {}.".format(junto, inverso))
    print("Essa frase É UM PALÍNDROMO")
else:
    print("A frase que você digitou foi {}, e o inverso dessa frase é {}.".format(junto, inverso))
    print("Essa frase NÃO É UM PALÍNDROMO")
