preco=float(input('Informe o preco do produto em R$:'))
print('Escolha uma opcao de pagamento:\n'
      '1 - Dinheiro/cheque\n'
      '2 - A vista no cartao\n'
      '3 - 2x no cartao\n'
      '4 - 3x ou mais no cartao')
pagamento=int(input('Digite o numero da opcao desejada:'))
if pagamento == 1:
    desconto=preco * 0.1
    preco=preco - desconto
    print('Voce recebeu 10% de desconto, o novo valor eh {}' .format(preco))
elif pagamento == 2:
    desconto=preco * 0.05
    preco=preco - desconto
    print('Voce recebeu 5%, o novo valor eh {}' .format(preco))
elif pagamento == 3:
    print('Opcao de pagamento aceita, valor {}' .format(preco))
elif pagamento == 4:
    aumento=preco * 0.2
    preco=preco + aumento
    print('Sera acrescentado 20% de juros no valor do produto devido a opcao de pagamento selecionada, novo valor {}' .format(preco))
else:
    print('Escolha uma opcao desejada')
print('FIM')
