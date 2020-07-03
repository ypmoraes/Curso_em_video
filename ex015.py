dias=int(input('Informe a quantidade de dias que vc passou com o carro:'))
km=float(input(('Informe a quantidade de KM que vc rodou:')))
vdias=(dias * 60)
vkm=(km * 0.15)
vfinal=(vdias + vkm)

print(('Tu gastou R$: {}' .format(vfinal)))