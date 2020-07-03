nome = str (input('Qual o seu nome?')).strip()
if nome == 'Yuri':
        print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome eh bem popular no Brasil')
elif nome in ('Juliana Mariana Ana Claudia'):
    print('Nome feminino bonito')
else:
    print('Seu nome eh bem normal')
print('Tenha um bom dia, {}!' .format(nome))
