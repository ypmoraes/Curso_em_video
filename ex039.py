import datetime

anonasc=int(input('Informe seu ano de nascimento:'))
ano=datetime.datetime.now().year
idade=ano - anonasc
print('Voce possui {} anos'.format(idade))

if idade < 18:
    print('Voce tera que se alistar no servico militar daqui {} anos' .format((18 - idade)))
elif idade == 18:
    print('Voce deve se alistar no servico militar esse ano')
elif idade > 18:
    print('Voce provavelmente se alistou no servico militar {} anos atras' .format((idade - 18)))
print('Fim')
