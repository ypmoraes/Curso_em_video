'''
########################################################################################
##      Enunciado:Rafaca o desafio 051, lendo o primeiro termo e a razao de uma PA,   ##
##      mostrando os 10 primeiros termos da progressao usando a estrutura while.      ##
##                                                                                    ##
##      Criado por: Yuri Moraes                                                       ##
##      Data:09/06/20                                                                 ##
##      Email:yuri_ppm@hotmail.com                                                    ##
########################################################################################
'''

termo=int(input('Insira o primeiro termo da PA:'))
razao=int(input('Insira a razao desta PA:'))
c=0
pa = 0

while c <= 9:
    pa = termo + (razao * c)
    c = c+1
    print(pa)
print('Fim')

'''Versao Guanabara
print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razao da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    cont += 1
print('FIM')'''
