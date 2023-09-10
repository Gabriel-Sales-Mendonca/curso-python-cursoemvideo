print("-"*20)
casa = float(input("Qual o valor da casa ? R$"))
salario = float(input("Qual o salário do comprador ? R$"))
tempo_ano = float(input("Em quantos anos o comprador deseja pagar ?"))

tempo_mes = tempo_ano * 12
mensalidade = casa / tempo_mes
salario_trinta = (30 / 100) * salario

if mensalidade > salario_trinta:
    print("Empréstimo negado, mesalidade excede 30% do salário do comprador")
else:
    print("O empréstimo pode ser concedido!!!")
print("-"*20)
