numero=int(input('Insira um numero'))
parouimpar=numero % 2

if parouimpar == 0:
    print('Voce digitou {} que eh um numero par' .format(numero))
else:
    print('Voce digitou {} que eh um numero impar' .format(numero))
print('Fim do script')
