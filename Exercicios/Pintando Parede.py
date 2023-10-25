larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
print('A parede tem a dimensão de {:.1f}x{:.1f} e sua area é de {:.2f}m².'.format(larg, alt, area))
tinta = area / 2
print('Para pintar a parede vai precisar de {:.1f}litros de tinta.'.format(tinta))