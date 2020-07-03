'''
Criado 15/06
'''

n = int(input('Digite um numero para fazermos a tabuada:'))
c = 1
while True:
    if n < 0:
        break
    print(f'{n} x {c} = {n * c}')
    c=c+1
    if c == 11:
        print('=' * 15)
        n=int(input('Digite um numero para fazermos a tabuada:'))
        c = 1
        if n < 0:
            break
print('Programa finalizado, muito obrigado.')