import random

aluno1=str(input('Insira o nome do aluno 1:'))
aluno2=str(input('Insira o nome do aluno 2:'))
aluno3=str(input('Insira o nome do aluno 3:'))
aluno4=str(input('Insira o nome do aluno 4:'))
lista=[aluno1, aluno2, aluno3, aluno4]

sorteado=random.choice(lista)

print('O aluno sorteado foi: {}' .format(sorteado))