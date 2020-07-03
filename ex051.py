'''
########################################################################################
##      Enunciado: Desenvolva um programa que leia o primeiro termo e a               ##
##      razao de uma PA. No final, mostre os 10 primeiros termos dessa progressao     ##
##                                                                                    ##
##      Criado por: Yuri Moraes                                                       ##
##      Data:05/06/20                                                                 ##
##      Email:yuri_ppm@hotmail.com                                                    ##
########################################################################################
'''

termo=int(input('Insira o primeiro termo da PA:'))
razao=int(input('Insira a razao desta PA:'))
decimo= termo + (10 -1) *razao
for c in range(termo, decimo + razao, razao):
    print(c)
