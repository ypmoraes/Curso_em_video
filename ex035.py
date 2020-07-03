r1=float(input('Insira o valor da linha 1:'))
r2=float(input('Insira o valor da linha 2:'))
r3=float(input('Insira o vlaor da linha 3:'))

if r1 < r2 +r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Eh possivel formar um triangulo')
else:
    print('Nao eh possivel formar triangulo')
