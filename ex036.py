valorcasa=float(input('Insira o valor da casa R$:'))
salario=float(input(('Insira o valor do salario R$:')))
qtdanos=int(input('Insira a quantidade anos que deseja pagar a casa:'))
prestacao=(valorcasa / (qtdanos * 12))

print('Iniciando sua avaliacao de Credito')
print('A Prestacao custara {:.2f} por Mes'.format(prestacao))
if (salario * 0.3) > prestacao:
    print('Seu emprestimo foi aprovado! Parabens!!!')
else:
    print('Seu emprestimo nao foi aprovado. Consulte seu gerente.')
print('Fim do sistema')
