import datetime

anonasc=int(input('Insira o seu ano de nascimento:'))
anoatual=datetime.datetime.now().year
idade=anoatual - anonasc
print('Sua idade eh: {}'.format(idade))

if idade <= 9:
    print('Sua categoria eh: Mirim')
elif idade <=14:
    print('Sua categoria eh: Infantil')
elif idade <= 19:
    print('Sua categoria eh: Junior')
elif idade <= 20:
    print('Sua categoria eh: Senior')
else:
    print('Sua categoria eh: Master')
print('Fim')