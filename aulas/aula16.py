lanche = ('Hamburger', 'Suco', 'Pizza ','Pudim')
# tuplas sao imutaveis

# print(sorted(lanche))
#
# print(lanche[1:3]) #as posicoes seriam 0, 1, 2 e 3. Ele para antes da ultima

for cont in range (0, len(lanche)):
    print(lanche[cont])

for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi mto')

for pos, comida in enumerate (lanche):
    print(f'Eu vou comer {comida} na posicao {pos}')

a = (5, 4, 8, 1)
b = (3, 2, 1, 5)
c = a + b
print(c)
print(c.count(5)) #quantas vezes aparece o numero 5
print(c.index(8)) #posicao do numero 8

pessoa = ('Yuri', 23, 'M', 77.3) # aceita dados de diferentes dipos
print(pessoa)
del pessoa #para apagar a tupla inteira
print(pessoa)