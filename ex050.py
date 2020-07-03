'''
########################################################################################
##      Enunciado:Desenvola um programa que leia seis numeros inteiros e              ##
##      mostre a soma apenas daqueles que forem pares.                                ##
##      se o valor digitador for impar, desconsidere-o                                ##
##                                                                                    ##
##      Criado por: Yuri Moraes                                                       ##
##      Data:05/06/20                                                                 ##
##      Email:yuri_ppm@hotmail.com                                                    ##
########################################################################################
'''

soma=0
cont=0

for c in range (1, 7):
    var=int(input('Digite o {} numero:'.format(c)))
    if var % 2 == 0:
        soma+=var
        cont+=1
print('Voce informou {} numeros pares e a soma foi {}' .format(cont, soma))



