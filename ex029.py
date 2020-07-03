velocidade=int(input('Insira a velocidade do carro em Km/h:'))
multa=(velocidade - 80) * 7

if velocidade > 80:
    print('Voce ultrapassou o limite de velocidade (80Km/h), a multa eh R$7,00 por Km acima do limite.')
    print('Sua multa eh: R${}' .format(multa))
else:
    print('Voce esta dentro do limite de velocidade (80Km/h)')
print('Fim do script')
