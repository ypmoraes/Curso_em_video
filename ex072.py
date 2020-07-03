'''
########################################################################################
##      Enunciado: Crie um programa que tenha uma tupla totalmente preenchida         ##
##      com uma contagem por extenso, de zero até vinte.Seu programa deverá ler       ##
##      um número pelo teclado entre 0 e 20 e mostrá-lo por extenso."""               ##
##                                                                                    ##
##      Criado por: Yuri Moraes                                                       ##
##      Data:17/06/20                                                                 ##
##      Email:yuri_ppm@hotmail.com                                                    ##
########################################################################################
'''

numeros=('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
numimput=int(input('Informe um numero inteiro entre 0 e 20: '))
while numimput not in range (0, 20):
    numimput=int(input('Informe um numero inteiro entre 0 e 20: '))
print(f'Voce digitou o numero {numeros[numimput]}')
