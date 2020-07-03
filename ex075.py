num=(int(input('Insira o primeiro valor: ')),
     int(input('Insira o segundo valor: ')),
     int(input('Insira o terceiro valor: ')),
     int(input('Insira o quarto valor: ')))

print(f'Estes foram os numeros digitados {num}')
print(f'O numero 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O numero 3 foi digitado pela primeira vez na posicao {num.index(3)}')
else:
    print('O valor 3 nao foi digitado em nenuma posicao')
print('Estes foram os valores pares digitados: ', end=' ')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
