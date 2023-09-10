nome = str(input("Digite o nome do colaborador: "))
salario = float(input('Digite o salário do colaborador: '))

if(0 <= salario <= 280):
    desconto = 0.2
    valor_desconto = 0.2 * salario
    novo_salario = salario + valor_desconto


print('O novo salário de {}, é de {:.2f}'.format(nome.upper(),novo_salario))
