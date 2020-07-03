salario=float(input("Informe seu salario:"))

if salario >= 1250:
    salarioaumento=salario + (salario * 0.10)
    print('Este eh o seu novo salario com 10% de aumento {:.2f}' .format(salarioaumento))
else:
    salarioaumento=salario + (salario *0.15)
    print('Este eh o seu novo salario com 15% de aumento {:.2f}' .format(salarioaumento))
print('Fim')