larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))

area = larg * alt
litros = area / 2

print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².\nPara pintar essa parede, você precisará de {:.2f}l de tinta.'.format(larg, alt, area, litros))
