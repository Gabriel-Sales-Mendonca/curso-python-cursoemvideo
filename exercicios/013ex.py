# Calculando o aumento de um funcionário
sal = float(input('Qual é o salário do funcionário: R$'))
sal_aumento = sal + (15/100 * sal)

print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}!'.format(sal, sal_aumento))
