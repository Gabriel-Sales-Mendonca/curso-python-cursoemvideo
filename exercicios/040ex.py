nota1 = float(input("Qual o valor da primeira nota ? "))
nota2 = float(input("Qual o valor da segunda nota ? "))
media = (nota1 + nota2) / 2

if media < 5:
    print(f"Sua média foi de {media}.")
    print("REPROVADO")
elif 5 <= media <=6.9:
    print(f"Sua média foi de {media}.")
    print("RECUPERAÇÃO")
elif media > 6.9:
    print(f"Sua média foi de {media}.")
    print("APROVADO")
