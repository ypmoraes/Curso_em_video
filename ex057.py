'''
########################################################################################
##      Enunciado: Faca um programa que leia o sexo de uma pessoa, mas so aceite      ##
##      os valores 'M' ou 'F'. Caso esteja errado, peca a digitacao novamente         ##
##      ate ter um valor correto.                                                     ##
##                                                                                    ##
##      Criado por: Yuri Moraes                                                       ##
##      Data:09/06/20                                                                 ##
##      Email:yuri_ppm@hotmail.com                                                    ##
########################################################################################
'''

sexo = str(input('Insira o sexo de uma pessoa: [M/F] ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Opcao invalida: [M/F] ')).strip().upper()[0]
print('Opcao {} registrada com sucesso' .format(sexo))


