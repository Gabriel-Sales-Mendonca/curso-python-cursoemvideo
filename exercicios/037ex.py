num = int((input("Digite um número inteiro: ")))
print('''Escolha uma opção para converter o número que você digitou:
OPÇÃO [1] BINÁRIO
OPÇÃO [2] OCTAL
OPÇÃO [3] HEXADECIMAL''')
conversor = int(input("Digite o número que represente sua opção de conversão: "))

if conversor == 1:
    print("{} convertido para BINÁRIO é igual a {}".format(num, bin(num)[2:]))
elif conversor == 2:
    print("{} convertido para OCTAL é igual a {}".format(num, oct(num)[2:]))
elif conversor == 3:
    print("{} convertido para HEXADECIMAL é igual a {}".format(num, hex(num)[2:]))
else:
    print("Opção inválida, tente novamente!")
