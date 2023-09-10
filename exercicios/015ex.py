# Calculando o valor a pagar pelo o aluguel de um carro
km = float(input('Informe quantos Km o carro percorreu: '))
dias = int(input('informe por quantos dias o carro ficou alugado: '))

pagar = (km * 0.15) + (dias * 60)

print('O total a pagar é de R${:.2f}'.format(pagar))
