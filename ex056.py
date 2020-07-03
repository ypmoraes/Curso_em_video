'''
########################################################################################
##      Enunciado:Desenvolva um programa que leia o nome, idade e sexo                ##
##      de 4 pessoas. No final do programa, mostre:                                   ##
##                                                                                    ##
##      - A media de idade do grupo                                                   ##
##      - Qual eh o nome do homem mais velho                                          ##
##      - Quantas mulheres tem menos de 20 anos                                       ##
##                                                                                    ##
##      Criado por: Yuri Moraes                                                       ##
##      Data:08/06/20                                                                 ##
##      Email:yuri_ppm@hotmail.com                                                    ##
########################################################################################
'''

media=0
countF=0
Mvelho=0
NomeVelho=''

for c in range (1, 5):
    print('---------{} Pessoa---------' .format(c))
    nome=str(input("Insira o seu nome:")).strip()
    idade=int(input("Digite sua idade:"))
    sexo=str(input("Qual seu sexo? (M) (F)")).upper().strip()
    media+=idade
    mediaidade=media/4
    if sexo=='M':
        if c == 1:
            Mvelho==idade
        else:
            if idade > Mvelho:
                Mvelho=idade
                NomeVelho=nome
    if sexo=='F' and idade <= 20:
        countF+=1
    else:
        print('Opcao invalida selecione M ou F')
    print("="*25)
print('A media de idade do grupo foi de {} anos' .format(mediaidade))
print('Das mulheres {} possuem menos de 20 anos' .format(countF))
print('A idade do homem mais velho eh de {} anos e seu nome eh {}'.format(Mvelho,NomeVelho))