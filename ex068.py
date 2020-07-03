'''
Criado 15/06
'''

from random import randint
print('Vamos jogar par ou impar?')
vitorias=0
resultado=''

while True:
    print('=' * 15)
    jogador=str(input('Voce quer par ou impar?')).upper().strip()[0]
    while jogador not in 'PI':
        print('Opcao invalida')
        jogador = str(input('Voce quer par ou impar?')).upper().strip()[0]
    njogador = int(input('Digite um numero:'))
    ncomputador=randint(0, 9)
    print(f'O computador jogou {ncomputador}')
    soma=njogador + ncomputador
    print(f'O resultado foi {soma}')
    if soma % 2 == 0:
        resultado='P'
        if resultado == jogador:
            print('Voce venceu')
            vitorias+=1
        else:
            print('Voce perdeu')
            resultado='Perdeu'
            break
    else:
        resultado='I'
        if resultado == jogador:
            print('Voce venceu')
            vitorias+=1
        else:
            print('Voce perdeu')
            resultado='Perdeu'
            break
    if resultado == 'Perdeu':
        break
print(f'Voce acomulou {vitorias} vitorias')
