soma_idade = 0
maior_idade_homem = 0
nome_homem = ""
mulher_menor_20 = 0
for c in range(1, 5):
    nome = str(input("nome da {}º pessoa: ".format(c)))
    idade = int(input("Idade da {}º pessoa: ".format(c)))
    sexo = str(input("Sexo da {}º pessoa: ".format(c)))
    soma_idade += idade
    if c == 1 and sexo in "Mm":
        maior_idade_homem = idade
        nome_homem = nome
    if sexo in "Mm" and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_homem = nome
    if sexo in "Ff" and idade < 20:
        mulher_menor_20 += 1
media = soma_idade / 4
print("A média das idades das pessoas é de {}".format(media))
print("O homem mais velho tem {} anos, e se chama {}".format(maior_idade_homem, nome_homem))
print("Tem {} mulheres menores do que 20 anos".format(mulher_menor_20))
