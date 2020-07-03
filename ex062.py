'''
########################################################################################
##      Enunciado:Melhore o desafio 061, perguntando para o usuario se ele quer       ##
##      mostrar mais alguns termos. O programa encerra quando ele disser              ##
##      que quer mostrar 0 termos                                                     ##
##                                                                                    ##
##      Criado por: Yuri Moraes                                                       ##
##      Data:09/06/20                                                                 ##
##      Email:yuri_ppm@hotmail.com                                                    ##
########################################################################################
'''

'''termo=int(input('Insira o primeiro termo da PA:'))
razao=int(input('Insira a razao desta PA:'))
decimo=9
c=0
user=1
while user != 0:
    while c <= decimo:
        pa= termo + (razao * c)
        c = c+1
        print(pa)

    user=int(input('Deseja continuar? Se sim, mais quantos numeros deseja mostrar? Se nao digite 0'))
    while c <= user + decimo:
        pa = termo + (razao * c)
        c=c+1
        print(pa)'''

primeiro=int(input('Insira o primeiro termo da PA:'))
razao=int(input('Insira a razao desta PA: '))
termo=primeiro
c = 1
user = 0
qtd=10
while qtd != 0:
    user = qtd + user
    while c <= user:
        print(termo)
        termo+=razao
        c+=1
    qtd=int(input('Deseja prosseguir com mais quantos termos?'))
print('A progressao foi finalizada com {} termos mostrados'.format(user))