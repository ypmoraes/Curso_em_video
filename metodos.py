#import math (importa todo o metodo)
from math import sqrt #importa apenas a funcao sqrt do metodo

num = int(input('Digite um numero:'))
raiz= sqrt(num) #se importado todo o metodo eh necessario utilizar math.sqrt

print('A raiz de {} eh igual a {}' .format(num, raiz))