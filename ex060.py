'''
########################################################################################
##      Enunciado: Faca um programa que leia um numero qualquer e mostre              ##
##      o seu fatorial. Ex:                                                           ##
##      5!=5x4x3x2x1=120                                                              ##
##                                                                                    ##
##      Criado por: Yuri Moraes                                                       ##
##      Data:09/06/20                                                                 ##
##      Email:yuri_ppm@hotmail.com                                                    ##
########################################################################################
'''

numero = int(input('Insira um numero inteiro para descobrir seu fatorial: '))
c = numero
fatorial= 1
print('Calculando {}! = '.format(numero), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    fatorial *= c
    c -= 1
print('{}'.format(fatorial))

''' Usando o for
numero = int(input('Insira um numero inteiro para descobrir seu fatorial: '))
fatorial=1
for c in range (numero, 0, -1):
    fatorial *=c
    print(c)
print(fatorial) '''

'''Versao Guanabara
from math import factorial
n = int(input('Digite um numero para calcular seu fatorial: '))
f = factorial (n)
print('O fatorial de {} eh {}.'.format(n, f))'''
