num1=int(input('Insira um numero inteiro:'))
num2=int(input('Insira outro numero inteiro:'))

if num1 > num2:
    print('Entre {} e {} o maior eh {}' .format(num1, num2, num1))
elif num2 > num1:
    print('Entre {} e {} o maior eh {}' .format(num1, num2, num2))
else:
    print('Estes numeros sao iguais')
print('Fim do script')