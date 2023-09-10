from datetime import date
ano_nascimento = int(input("Digite seu ano nascimeto: "))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento

if ano_atual >= ano_nascimento:
    if idade <= 9:
        print(f"Você tem {idade} anos, sua categoria é MIRIM")
    elif 9 < idade <= 14:
        print(f"Você tem {idade} anos, sua categoria é INFANTIL")
    elif 14 < idade <= 19:
        print(f"Você tem {idade} anos, sua categoria é JUNIOR")
    elif 19 < idade <= 25:
        print(f"Você tem {idade} anos, sua categoria é SÊNIOR")
    elif idade > 25:
        print(f"Você tem {idade} anos, sua categoria é MASTER")
else:
    print("Ano inválido, o ano que você digitou é superior ao ano atual, tente novamente!")
