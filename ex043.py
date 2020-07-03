import math

peso=float(input('Informe seu peso em KG:'))
altura=float(input('Informe sua altura em CM:'))
imc=peso / (altura ** 2)
print('{:.1f}'.format(imc))

if imc <= 18:
    print('Abaixo do peso')
elif 18 <= imc < 25:
    print('Peso ideal')
elif 25 <= imc < 30:
    print('Sobrepeso')
elif 30 <= imc < 40:
    print('Obesidade')
elif imc >= 40:
    print('Obesidade morbida')
print('Fim')



