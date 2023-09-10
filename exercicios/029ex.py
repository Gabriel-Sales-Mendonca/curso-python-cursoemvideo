velocidade = float(input("Qual foi a velocidade do carro ? "))
if(velocidade > 80):
    multa = (velocidade - 80) * 7
    print("Você foi multado!\nO valor total da multa é de R${:.2f}".format(multa))
else:
    print("Relaxa, você não foi multado!")
