produtos=('Lapis', 1.75,
          'Borracha', 2.00,
          'Caderno', 15.90,
          'Estojo', 25.00,
          'Transferidor', 4.20,
          'Compasso', 9.99,
          'Mochila', 120.32,
          'Canetas', 22.30,
          'Livro', 34.90)
print('-' * 40)
print(f'{"lista de precos"}')
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end=' ')
    else:
        print(f'R${produtos[pos]:>7.2f}')
print('-' * 40)

''' Versao youtube 
rodei o for com teste de tipagem: se é STR = produto se é FLOAT  = Preço
Ficou assim:
for i in listagem:
    if type(i) is str:
        print(f'{i:.<32}', end='')
    else:
        print(f'R$ {i:>5.2f}')
print('--'*20)
'''