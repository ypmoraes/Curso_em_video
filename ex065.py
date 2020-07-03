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
soma = 0
maior = 0
menor = 9999

opcao=str(input('Deseja comecar? [S/N]'))

while opcao not in 'Nn':
    user=int(input('Insira um valor inteiro:'))
    cont += 1
    soma += user
    if user > maior:
        maior = user
    if user < menor:
        menor = user
    opcao=str(input('Deseja continuar? [S/N]'))
#print(user)
#print(cont)
#print(soma)
print('A media entre os numeros digitados eh: {}' .format(soma/cont))
print('O maior numero digitado foi: {}' .format(maior))
print('O menor numero digitado foi: {}' .format(menor))