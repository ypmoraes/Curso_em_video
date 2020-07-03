'''
########################################################################################
##      Enunciado: Crie um programa que leia dois valores e mostre um menu na tela:   ##
##      [1] - Somar                                                                   ##
##      [2] - Multiplicar                                                             ##
##      [3] - Maior                                                                   ##
##      [4] - Novos numeros                                                           ##
##      [5] - Sair do programa                                                        ##
##      Seu programa devera realizar a operacao solicitada em cada caso               ##
##                                                                                    ##
##      Criado por: Yuri Moraes                                                       ##
##      Data:09/06/20                                                                 ##
##      Email:yuri_ppm@hotmail.com                                                    ##
########################################################################################
'''

num1=int(input('Insira um valor inteiro:'))
num2=int(input('Insira o segundo valor inteiro:'))

opcao=int(input('Escolha uma das seguintes operacoes: \n'
      '[1] - Somar\n'
      '[2] - Multiplicar\n'
      '[3] - Maior\n'
      '[4] - Novos numeros\n'
      '[5] - Sair do programa\n'
      'Digite o numero da opcao: '))
while opcao != 5:
    if opcao == 1:
        print('Voce esoclheu somar {} e {}' .format(num1, num2))
        print('A soma entre os dois valores eh: {}' .format(num1 + num2))
        opcao=int(input('Deseja realizar outra operacao? Se sim escolha de 1 a 4, se nao digite 5: '))
    elif opcao == 2:
        print('Voce escolheu multiplicar {} por {}' .format(num1, num2))
        print('O resultado da multiplicacao eh: {}' .format(num1 * num2))
        opcao = int(input('Deseja realizar outra operacao? Se sim escolha de 1 a 4, se nao digite 5: '))
    elif opcao == 3:
        print('Voce escolheu verificar qual o maior valor entra {} e {}' .format(num1, num2))
        if num2 > num1:
            print('O maior valor eh {}' .format(num2))
        else:
            print('O maior valor eh: {}' .format(num1))
        opcao = int(input('Deseja realizar outra operacao? Se sim escolha de 1 a 4, se nao digite 5: '))
    elif opcao == 4:
        print('Voce escolheu digitar novos numeros para sua operacao')
        num1 = int(input('Insira um novo valor inteiro:'))
        num2 = int(input('Insira o segundo novo valor inteiro:'))
        opcao = int(input('Deseja realizar outra operacao? Se sim escolha de 1 a 4, se nao digite 5: '))
    else:
        opcao=int(input('Opcao invalida, digite novamente uma opcao entre 1 e 5: '))
print('Voce escolheu sair do programa')


