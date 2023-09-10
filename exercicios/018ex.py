from math import sin, tan, cos, radians

ang = float(input('Digite o valor de ângulo: '))

ang = radians(ang)
sen = sin(ang)
tang = tan(ang)
coss = cos(ang)

print('Seno: {}\nCosseno: {}\nTangente: {}'.format(sen, coss, tang))
