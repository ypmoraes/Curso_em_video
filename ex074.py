from random import randint


tupla = randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10)
menor = maior = 0

print(f'Estes foram os numeros gerados pelo computador {tupla}')

for pos, c in enumerate (tupla):
    #Menor
    if pos == 1:
        menor = tupla[0]
    elif menor > tupla[1]:
        menor = tupla [1]
    elif menor > tupla[2]:
        menor = tupla[2]
    elif menor > tupla [3]:
        menor = tupla [3]
    elif menor > tupla [4]:
        menor = tupla[4]
    #Maior
    if pos == 1:
        maior = tupla[0]
    elif maior < tupla[1]:
        maior = tupla[1]
    elif maior < tupla[2]:
        maior = tupla [2]
    elif maior < tupla[3]:
        maior < tupla[3]
    elif maior < tupla[4]:
        maior = tupla[4]
print(f'Destes numeros o menor foi {menor} e o maior foi {maior}')

'''versao guanabara
from random import randint
numeros = randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10)
print('Os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n}', end='')
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min((numeros))}')'''