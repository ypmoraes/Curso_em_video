import random

aluno1=str(input('Insira o nome do aluno 1:'))
aluno2=str(input('Insira o nome do aluno 2:'))
aluno3=str(input('Insira o nome do aluno 3:'))
aluno4=str(input('Insira o nome do aluno 4:'))

lista=[aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)

print('A ordem eh: {}' .format(lista))
