'''
########################################################################################
##      Enunciado:                                                   ##
##                                                                                    ##
##      Criado por: Yuri Moraes                                                       ##
##      Data:09/06/20                                                                 ##
##      Email:yuri_ppm@hotmail.com                                                    ##
########################################################################################
'''
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
n = int(input('Quantos termos voce quer mostrar?'))
t1 = 0
t2 = 1
print('{} - {}'.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print('- {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont +=1
print('- Fim')
