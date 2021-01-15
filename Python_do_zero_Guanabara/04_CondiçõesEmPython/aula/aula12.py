
#condição simples
nome = str(input('Qual é o seu nome? '))
if nome == 'Henrique':
    print('Que nome Bonito')
print(f'Tenha um bom dia! {nome}')

#condiçao composta
nome = str(input('Qual é o seu nome? '))
if nome == 'Henrique':
    print('Que nome Bonito')
else:
    print('Seu nome é bem normal.')
print(f'Tenha um bom dia! {nome}')

#estrutura condicional 
nome = str(input('Qual é o seu nome? '))
if nome == 'HENRIQUE':
    print('Que nome Bonito')
elif nome == 'AMANDA' or nome == 'GABRIEL' or nome == 'EDILA':
    print('Seu nome é bem popular no Brasil!')
elif nome in 'MARIA ALEXANDRA': # in o que estiver dentro dos nomes será apresentado
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal.')
print(f'Tenha um bom dia! {nome}')