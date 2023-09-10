#Algoritmo que lê o preço de um produto e aplica um desconto de 5%
produto = float(input('Digite o valor do produto: R$'))

# Calculando o valor após o desconto
desconto = produto - (5/100 * produto)

print('O preço do produto após o desconto é de R${:.2f}!'.format(desconto))
