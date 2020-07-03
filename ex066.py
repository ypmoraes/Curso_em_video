'''
Criado 15/06
'''

cont=0
soma=0
n = 0
while True:
    n=int(input('Insira um numero: (999 para parar)'))
    if n == 999:
        break
    soma+= n
    cont+=1
print(f'Foram digitados {cont} numeros e a soma dos numeros digitados foi: {soma}')