import random
from time import sleep

numpc=random.randint(0 , 5)
#print(numpc)
numinput=int(input('Estou pensando em um numero de 1 a 5.... Consegue adivinhar qual?'))
print('Processando')
sleep((1))
if numpc == numinput:
    print('Incrivel... Voce acertou')
else:
    print('Muito ruim...')
    print('Eu estava pensando em {}' .format(numpc))
print('Execute o script novamente para realizar outra tentativa')


