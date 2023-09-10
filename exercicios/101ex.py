def voto(ano):
    from datetime import date
    global idade
    idade = date.today().year - ano
    return idade


voto(int(input('Digite seu ano de nascimento: ')))

if idade > 18 and idade < 65:
    print('Seu voto é OBRIGATÓRIO')
elif 16 <= idade < 18 or idade >= 65:
    print('Seu voto é OPCIONAL')
else:
    print('Seu voto ainda é NEGADO')