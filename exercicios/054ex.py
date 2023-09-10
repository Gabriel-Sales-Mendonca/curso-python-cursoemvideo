from datetime import date

qtd_maior = 0
qtd_menor = 0

for c in range(7):
    nascimento = int(input("Digite o ano de nascimento da pessoas: "))
    idade = date.today().year - nascimento
    if idade >= 18:
        qtd_maior += 1
    else:
        qtd_menor += 1
print("{} pessoa(s) são MAIORES DE IDADE".format(qtd_maior))
print("{} pessoa(s) ainda são MENORES DE IDADE".format(qtd_menor))
