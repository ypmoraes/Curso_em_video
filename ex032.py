from datetime import date

ano=int(input('Insira o ano que deseja saber se eh ou nao bissexto ou coloque 0 para analisar o ano atual:'))

if ano == 0:
    ano = date.today().year

div4= ano % 4

if div4 == 0:
    div100= ano % 100
    if div100 > 0:
        print('Ano bissexto')
    else:
        print('Ano nao bissexto')
else:
    div400=ano % 400
    if div400 == 0:
        print('Ano bissexto')
    else:
        print('Ano nao bissexto')
print('fim do script')
