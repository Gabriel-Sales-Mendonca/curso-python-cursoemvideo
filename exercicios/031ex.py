distancia = float(input("Qual é a distância da sua viagem em Km ? "))
if distancia <= 200:
    preco = distancia * 0.5
    print("O preço da passagem para a sua viagem é de R${:.2f}".format(preco))
else:
    valor = distancia * 0.45
    print("O preço da passagem para a sua viagem é de R${:.2f}".format(valor))
