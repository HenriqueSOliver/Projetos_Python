
galera = [] # principal
dados = [] #lista temporaria
maiop = menorp = 0 


while True:
    dados.append(str(input('Digite um nome: ')))
    dados.append(int(input('Digite Peso: ')))
    if len(galera) == 0 :
        maiop = menorp = dados[1]
    else:
        if dados[1] > maiop:
            maiop = dados[1]
        if dados[1] < menorp:
            menorp = dados[1]


    galera.append(dados[:])
    dados.clear()
    
    r = ' '
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if r == 'N':
        break
    print('-='*50)
print(galera)

print('-='*50)

print(f'Você digitou os valores {galera}')

print('-='*50)

print(f'Ao todo, você cadastrou {len(galera)} pessoas.')
print(f'O maior peso digitado foi {maiop}Kg. Peso de ', end='')
for p in galera:
    if p[1] == maiop:
        print(f'{p[0]}', end=' ')
print()

print(f'\nO menor peso digitado foi {menorp}Kg. nas posição ', end='')
for p in galera:
    if p[1] == menorp:
        print((f'{p[0]}'), end =' ')




