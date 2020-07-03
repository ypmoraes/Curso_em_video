altura=float(input('Insira a altura da parede:'))
largura=float(input('Insira a largura da parede:'))
area=largura*altura
print('A area da parede eh:', area)
print('Sera necessario {} litros de tinta' .format(area/2))