from math import hypot

cat1 = float(input('Digite o valor do cateto oposto: '))
cat2 = float(input('Digite o valor do cateto adjacente: '))

hip = hypot(cat1, cat2)

print('O comprimento da hipotenusa é: {}'.format(hip))
