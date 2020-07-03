import math

catetoOP=float(input('Insira a medida do cateto oposto em cm:'))
catetoAD=float(input('Insira a medida do cateto adjacente em cm:'))
hipotenusa=(math.hypot(catetoAD, catetoAD))
#hipotenusa=(((catetoOP ** 2) + (catetoAD **2))**(1/2))

print('{:.2f}' .format(int(hipotenusa)))
