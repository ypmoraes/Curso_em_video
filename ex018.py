from math import radians, sin, cos, tan
angulo= float(input('Digite o angulo:'))
seno= sin(radians(angulo))
print('O Angulo de {} tem o SENO de {:.2f}' .format(angulo, seno))
cosseno= cos(radians(angulo))
print('O Angulo de {} tem cosseno de {:.2f}' .format(angulo,cosseno))
tangente= tan(radians(angulo))
print('O angulo de {} tem a Tangente de {:.2f}' .format(angulo, tangente))
