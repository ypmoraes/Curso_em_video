nomecidade=str(input('Insira o nome da cidade:'))
nomeseparado=nomecidade.split()
primeironome=nomeseparado[0].upper()
santo='SANTO' in primeironome

print('O primeiro nome eh santo? {}' .format(santo))