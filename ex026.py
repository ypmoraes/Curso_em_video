frase=str(input('Insira uma frase:')).upper().strip()

print('Quantidade de letras A: {}' .format(frase.count('A')))
print('Posicao q A aparece pela primeira vez: {}' .format(frase.find('A')+1))
print('Posicao q A aparece pela ultima vez: {}' .format(frase.rfind('A')+1))




