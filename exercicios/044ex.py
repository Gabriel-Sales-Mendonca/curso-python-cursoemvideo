valor = float(input("Qual o preço do produto: "))
pagamento = int(input('''Leia as opções de forma de pagamento abaixo e digite o número correspondente a opção que você deseja:
opção 1 - à vista dinheiro/cheque;
opção 2 – à vista no cartão;
opção 3 – em até 2x no cartão;
opção 4 – 3x ou mais no cartão
'''))

if pagamento == 1 or pagamento == 2 or pagamento == 3 or pagamento == 4:
    valor_final = 0
    if pagamento == 1:
        valor_final = valor - (10 / 100 * valor)
    elif pagamento == 2:
        valor_final = valor - (5 / 100 * valor)
    elif pagamento == 3:
        valor_final = valor
        print("O valor a pagar são duas parcelas de R${:.2f} sem juros ".format(valor / 2))
    elif pagamento == 4:
        parcelas = int(input("Serão quantas parcelas ? "))
        valor_final = valor + (20 / 100 * valor)
        valor_parcelas = valor_final / parcelas
        print("O valor a pagar são {} parcelas de R${:.2f}".format(parcelas, valor_parcelas))
    print("A sua compra de R${:.2f} sairá por R${:.2f}".format(valor,valor_final))
else:
    print("Opção incorreta, tente novamente")
