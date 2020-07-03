viagem=int(input('Insira a distacia da sua viagem em Km:'))
if viagem <= 200:
    valorcobrado=viagem * 0.50
else:
    valorcobrado=viagem * 0.45
print('Sua viagem ira custar {}' .format(valorcobrado))
print('Fim do script')
