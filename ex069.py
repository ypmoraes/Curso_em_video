contidade=0
conthomem=0
contmulheres=0
sexo=''

while True:
    idade=int(input('Informe sua idade:'))
    sexo = str(input('Infome seu sexo: [M/F]')).upper().strip()[0]
    while sexo not in 'MF':
        print('Opcao invalida')
        sexo = str(input('Infome seu sexo: [M/F]')).upper().strip()[0]
    opcao=str(input('Deseja continuar?')).upper().strip()
    while opcao not in 'SN':
        print('Opcao invalida')
        opcao = str(input('Deseja continuar?')).upper().strip()
    if idade > 18:
        contidade+=1
    if sexo == 'M':
        conthomem += 1
    if sexo == 'F' and idade > 20:
        contmulheres += 1
    if opcao in 'N':
        break
print(f'Foram cadastrados {contidade} pessoas com mais de 18 anos.')
print(f'Foram cadastrados {conthomem} homens. Tambem foi cadastrado {contmulheres} com mais de 20 anos')

