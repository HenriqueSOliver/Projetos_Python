#dicionário simples

pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(pessoas)
print(pessoas['nome'])
print(pessoas['sexo'])
print(pessoas['idade'])
print(f'o {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

for k in pessoas.keys():
    print(k)

for k in pessoas.values():
    print(k)

for k, v in pessoas.items():
    print(f'{k} = {v}')

#mudar o nome
pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
pessoas['nome'] = 'Leandro'
for k, v in pessoas.items():
    print(f'{k} = {v}')

pessoas['peso'] = 98.5 #adicionar uma key e valores
for k, v in pessoas.items():
    print(f'{k} = {v}')


del pessoas['sexo']
for k, v in pessoas.items():
    print(f'{k} = {v}')

#criar um dicionário dentro de uma lista
brasil = [] #lista
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'} #dicionário
estado2 = {'uf': 'São Paulo', 'sigla': "SP"} #dicionário

brasil.append(estado1)
brasil.append(estado2)

print(estado1)
print(estado2)
print(brasil) #vai mostrar a lista inteira
print(brasil[0]) # vai mostrar o rio de Janeiro
print(brasil[1]) # vai mostrar São paulo
print(brasil[0]['uf']) #vai trazer uf do Rio
print(brasil[1]['sigla']) # vai trazer SP


#interessante
estado = {} #dicionário
brasil = [] #lista
for c in range(0,3): #vou ler 3 estados
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy()) # para dicionário tem q usar .copy
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')
