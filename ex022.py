nome=str(input('Insira seu nome completo:')).strip()
nomesemespaco=nome.split()
nomesemespaco2=''.join(nomesemespaco)
primeironome=nomesemespaco[0]

print('Este eh o nome em maiusculo: {}' .format(nome.upper()))
print('Este eh o nome em minusculo: {}' .format(nome.lower()))
print('Quantidade de letras no nome: {}' .format(len(nomesemespaco2)))
print('Quantidade letras do primeiro nome:{}' .format(len(primeironome)))

