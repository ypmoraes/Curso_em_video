'''
########################################################################################
##      Enunciado: Melhore o jogo do Desafio 028 onde o computador vai "pensar"       ##
##      em um numero entre 0 e 10. So que agora o jogador vai tentar adivinhar ate    ##
##      acertar, mostrando no final quantos palpites foram necessarios para vencer.    ##
##                                                                                    ##
##      Criado por: Yuri Moraes                                                       ##
##      Data:09/06/20                                                                 ##
##      Email:yuri_ppm@hotmail.com                                                    ##
########################################################################################
'''

from random import  randint
from time import sleep

numpc=randint(1, 10)
print('Estou pensando em um numero!')
sleep(2)
numjogador=int(input('Pensei em um numero inteiro de 1 a 10. Consegue adivinhar?'))
countErros=0

while numjogador != numpc: #Daria para fazer while not
    if numjogador <= numpc:
        numjogador=int(input('Errado, meu numero eh maior, digite novamente seu numero:'))
    elif numjogador >= numpc:
        numjogador=int(input('Errado, meu numero eh menor, digite novamente seu numero:'))
    countErros+=1
print('Parabens!! Eu realmente estava pensando no numero {}!!' .format(numpc))
print('Voce precisou de {} tentativas'.format(countErros+1))

''' Versao Guanabara
from  random import  randint
computador = randint (0 ,10)
print('Sou seu computador... Acabei de pensar em um numero entre 0 e 10.')
print('Sera que voce consegue adivinhar qual foi?')
acertou= False
palpites = 0

while not acertou:
    jogador = int(input('Qual seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais.... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos.... Tente mais uma vez.')
print('Acertou com {} tentativas. Parabens!' .format(palpites))
'''