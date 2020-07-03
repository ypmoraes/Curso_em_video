'''
########################################################################################
##      Enunciado: Crie um programa que leia o ano de nascimento de sete pessoas.     ##
##      no final, mostre quantas pessoas ainda nao atingiram a maioridade e           ##
##      quantas ja sao maiores.                                                       ##
##                                                                                    ##
##      Criado por: Yuri Moraes                                                       ##
##      Data:05/06/20                                                                 ##
##      Email:yuri_ppm@hotmail.com                                                    ##
########################################################################################
'''

from datetime import date
qtdm=0
qtdM=0

for c in range (0, 7):
    nome=str(input('Digite seu nome:'))
    anonasc=int(input('Digite o seu ano de nascimento:'))
    idade= date.today().year - anonasc
    if idade >= 21:
        qtdM+=1
    elif idade <=20:
        n=1
        qtdm+=1
print("Este eh o numero de pessoas com maioridade {}" .format(qtdM))
print("Este eh o numero de pessoas que nao atingiram a maioridade {}" .format(qtdm))
