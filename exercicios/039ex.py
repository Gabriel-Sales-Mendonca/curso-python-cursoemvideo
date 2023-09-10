import datetime
ano_nascimento = int(input("Digite o seu ano de nascimento: "))
ano_atual = datetime.datetime.now().year
idade = ano_atual - ano_nascimento

if ano_nascimento <= ano_atual:
    if idade < 18:
        tempo_resta = 18 - idade
        print(f'''Quem nasceu em {ano_nascimento} tem {idade} anos.
Você ainda vai se alistar para o serviço militar, falta(m) {tempo_resta} ano(s).''')
    elif idade == 18:
        print(f'''Quem nasceu em {ano_nascimento} tem {idade} anos.
Está na hora de você se alistar ao serviço militar''')
    else:
        tempo_passou = idade - 18
        print(f'''Quem nasceu em {ano_nascimento} tem {idade} anos.
já se passaram {tempo_passou} ano(s) do prazo para você se alistar''')
else:
    print("Ano inválido, o ano que você digitou é superior ao ano atual, tente novamente!")
