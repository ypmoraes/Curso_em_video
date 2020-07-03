'''
########################################################################################
##      Enunciado: Refaca o Desafio 009, mostrando a tabuada de um numero             ##
##      que o usuario escolher, so que adora utilizando um laco for.                  ##
##                                                                                    ##
##      Criado por: Yuri Moraes                                                       ##
##      Data:05/06/20                                                                 ##
##      Email:yuri_ppm@hotmail.com                                                    ##
########################################################################################
'''

num1=int(input('Insira o numero que voce deseja saber a tabuada:'))
for c in range (1, 11):
    print('{} multiplicado por {} eh igual a {}'.format(num1, c, num1*c ))