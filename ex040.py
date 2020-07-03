nota1=float(input('Insira a nota 1:'))
nota2=float(input('Insira a nota 2:'))
media=(nota1 + nota2)/2
print('Sua media foi: {}' .format(media))

if media < 5.0:
    print('Vc foi: Reprovado')
elif media > 7.0:
    print('Vc foi: Aprovado')
else:
    print('Vc ficou de: Recuperacao')
print('Fim')
