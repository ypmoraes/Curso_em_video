'''
########################################################################################
##      Enunciado: Crie um programa que leia uma frase qualquer e diga                ##
##      se ela eh um palindromo, desconsiderando os espacos                           ##
##                                                                                    ##
##      Criado por: Yuri Moraes                                                       ##
##      Data:06/06/20                                                                 ##
##      Email:yuri_ppm@hotmail.com                                                    ##
########################################################################################
'''

var1=str(input('Insira uma frase para descobrir se eh um palindromo:')).strip().upper()
palavras=var1.split()
junto=''.join(palavras)
inverso=''
for letra in range (len(junto) -1, -1, -1):
    inverso+=junto[letra]
if junto == inverso:
    print('Esta frase forma um palindromo {} {}' .format(junto, inverso))
else:
    print('Esta frase nao forma um palindromo {} {}' .format(junto, inverso))
