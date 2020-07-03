numero=int(input('Insira um numero inteiro:'))
print('Voce deseja converter esse numero para qual das bases \n'
      '1 - Para binario \n'
      '2 - Para Octal \n'
      '3 - Para Hexadecimal')
op=int(input('Insira a opcao desejada:'))

if op == 1:
    print('O numero {} convertido para binario eh {}' .format(numero, bin(numero)[2:]))
elif op == 2:
    print('O numero {} convertido para octal eh {}' .format(numero, oct(numero)[2:]))
elif op == 3:
    print('O numero {} convertido para hexadecimal eh {}' .format(numero, hex(numero).upper()[2:]))
else:
    print('Escolha uma das opcoes anteriores')
print('Fim do script')



