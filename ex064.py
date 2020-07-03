'''
########################################################################################
##      Enunciado:Melhore o desafio 061, perguntando para o usuario se ele quer       ##
##      mostrar mais alguns termos. O programa encerra quando ele disser              ##
##      que quer mostrar 0 termos                                                     ##
##                                                                                    ##
##      Criado por: Yuri Moraes                                                       ##
##      Data:12/06/20                                                                 ##
##      Email:yuri_ppm@hotmail.com                                                    ##
########################################################################################
'''

cont = 0
user = 0
soma=0
user=int(input('Digitie um numero inteiro: '))
while user != 999:
    soma += user
    cont+=1
    user = int(input('Digitie um numero inteiro: '))
print('Foram digitados {} ateh chegar no 999' .format(cont))
print('A soma destes numeros foi {}' .format(soma))