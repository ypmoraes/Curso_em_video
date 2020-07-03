'''
########################################################################################
##      Enunciado: Faca um programa que leia um numero inteiro e diga se              ##
##      ele eh ou nao um numero primo                                                 ##
##                                                                                    ##
##      Criado por: Yuri Moraes                                                       ##
##      Data:06/06/20                                                                 ##
##      Email:yuri_ppm@hotmail.com                                                    ##                                                                                    ##
########################################################################################
'''

num1=int(input('Digite um numero:'))
cont=0
for c in range(1, num1+1):
    if num1 % c ==0:
        print("Este numero foi divisivel por {}" .format(c))
        cont+=1
    else:
        print("Este numero nao foi divisivel por {}".format(c))
print("Este numero foi divisivel {} vezes" .format(cont))
if cont == 2:
    print("Este numero eh primo")
else:
    print("Este numero nao eh primo")




