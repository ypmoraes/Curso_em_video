total = milreais = menor = cont = 0
barato=''

while True:
    nomeprod=str(input('Informe o nome do produto: '))
    preco=float(input('Informe o preco do produto: R$ '))
    total+=preco
    cont+=1
    if preco > 1000:
        milreais+=1
    if cont == 1 or menor > preco:
        menor = preco
        barato = nomeprod
    opcao=str(input('Deseja continuar?')).upper().strip()[0]
    while opcao not in 'SN':
        print('Opcao invalida')
        opcao = str(input('Deseja continuar?')).upper().strip()[0]
    if opcao == 'N':
        break
print(f'O seu total foi: R${total}. Voce comprou {milreais} produtos acima de mil reais')
print(f'O produto mais barato custa foi {barato} que custou R${menor}')