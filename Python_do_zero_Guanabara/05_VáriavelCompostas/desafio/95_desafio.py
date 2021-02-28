time = []
jogador = {}
gols = []

while True:
    jogador.clear()
    jogador['Nome'] = str(input('Nome do Jogador: '))
    qtd = int(input(f'Quantas partidas {jogador["Nome"]} Jogou? '))
    gols.clear()
    for c in range (0, qtd):
        gols.append(int(input(f'Quantos gols na {c+1} partida: ')))
    jogador['Gols'] = gols[:]
    jogador['Total de Gols'] = sum(gols)
    time.append(jogador.copy())
    while True:
        r = str(input('Quer continuar [S/N]: ')).upper()[0]
        if r in 'SN':
            break
        print('[ERRO] - Responda apenas S ou N: ')
    if r == 'N':
        break
print('-='*40)
print('Cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-='*40)
for k, v in enumerate(time):
    print(f'{k:>4} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-='*40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar)'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'[ERRO] - Não existe jogador com código {busca}')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["Nome"]}:')
        for i, g in enumerate(time[busca]['Gols']):
            print(f'     No jogo {i+1} fez {g} gols.')
    print('-='*40)
print('<<< VOLTE SEMPRE >>>')