expressao = str(input('Digite uma expressão matemática que use parênteses: '))
aberto = expressao.count('(')
fechado = expressao.count(')')
if aberto == fechado:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
