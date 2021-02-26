jogador = {}
gols = []

jogador['Nome'] = str(input('Nome do Jogador: '))
qtd = int(input(f'Quantas partidas {jogador["Nome"]} Jogou? '))
for c in range (0, qtd):
    gols.append(int(input(f'Quantos gols na {c+1} partida: ')))
jogador['Gols'] = gols[:]
jogador['Total de Gols'] = sum(gols)

print('-='*20)
print(jogador)
print('-='*20)

for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*20)

print(f'O jogador {jogador["Nome"]} participou de {c+1} partidas.')
for i, v in enumerate(jogador['Gols']):
    print(f'  => Na {i+1}º partida , fez {v} gols.')
print(f'  => Foi um total de {jogador["Total de Gols"]} gols.')