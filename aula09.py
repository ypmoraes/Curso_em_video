#Fatiamento

frase='Curso em video Python'
print(frase)
print(frase[9:]) #Mostra da posicao 9 ateh o fim da string
print(len(frase)) #Mostra o tamanho da string

#analise

print(frase.count('o')) #quantidade de o (case sensitive)
print(frase.find('deo')) #mostra onde foi encontrado e qual a posicao que comeca
print(frase.find(('Android'))) #caso a string nao for encontrada o resultado sera -1
print(frase.rfind(A)) #busca da direita para esquerda
print('Curso' in frase) #Caso existir o retorno eh true

#Transformacao

print(frase.replace('Python', 'Android')) #substitui 1 por 2
print(frase.upper()) #substitui por letra maiuscula
print(frase.lower()) #substitui por letra minuscula
print(frase.capitalize())  #Deixa apenas a primeira letra em maiusculo, todo resto fica em minusculo
print(frase.title()) #toda a primeira letra fica maiuscula

frase2='   Aprenda Python  '

print(frase2.strip()) #remove os espacos indesejados
print(frase2.rstrip()) #remove os espacos indesejados da direita
print(frase2.lstrip()) #remove os espacos indesejados da esquerda

#Divisao

print(frase.split()) #gera um array com as palavras da string (caracter separador padrao eh o espaco)
print('-'.join(frase)) #junta

