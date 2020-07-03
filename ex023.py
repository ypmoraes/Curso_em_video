numero=int(input('Insira um numero:'))
u = numero // 1 % 10
d= numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10

print('O numero digitado foi: {}' .format(numero))
print('Unidade: {}' .format(u))
print('Dezena: {}' .format(d))
print('Centena: {}' .format(c))
print('Milhar: {}' .format(m))

