from random import choice

print('Vamos jogar jokenpo??\n'
      'Acha que consegue me vencer?')
jogador=str(input('Joookeenpoo!! Qual opcao voce jogou:')).upper()
computador=['PEDRA','PAPEL','TESOURA']
computchoice=choice(computador)

if jogador == 'PAPEL' and computchoice == 'PEDRA':
    print('Voce ganhou!!\n'
          'Voce escolheu {} e o computador escolheu {}' .format(jogador, computchoice))
elif jogador == 'PAPEL' and computchoice == 'TESOURA':
    print('Voce perdeu hahah\n'
          'Voce escolheu {} e o computador escolheu {}' .format(jogador, computchoice))
elif jogador == 'PAPEL' and computchoice == 'PAPEL':
    print('Empatou, vamos outra?\n'
          'Voce escolheu {} e o computador escolheu {}' .format(jogador, computchoice))
elif jogador == 'PEDRA' and computchoice == 'PEDRA':
    print('Empatou, vamos outra?\n'
          'Voce escolheu {} e o computador escolheu {}' .format(jogador, computchoice))
elif jogador == 'PEDRA' and computchoice == 'PAPEL':
    print('Voce perdeu hahah\n'
          'Voce escolheu {} e o computador escolheu {}' .format(jogador, computchoice))
elif jogador == 'PEDRA' and computchoice == 'TESOURA':
    print('Voce ganhou!!\n'
          'Voce escolheu {} e o computador escolheu {}'.format(jogador, computchoice))
elif jogador == 'TESOURA' and computchoice == 'PEDRA':
    print('Voce perdeu hahah\n'
          'Voce escolheu {} e o computador escolheu {}'.format(jogador, computchoice))
elif jogador == 'TESOURA' and computchoice == 'PAPEL':
    print('Voce ganhou!!\n'
          'Voce escolheu {} e o computador escolheu {}'.format(jogador, computchoice))
elif jogador == 'TESOURA' and computchoice == 'TESOURA':
    print('Empatou, vamos outra?\n'
          'Voce escolheu {} e o computador escolheu {}'.format(jogador, computchoice))
else:
    print('Escolha entre: Pedra, Papel e Tesoura')
print('fim')