from random import randint
from operator import itemgetter

jogadores = {'jogador-1': randint(1,6),
                'jogador-2': randint(1,6),
                'jogador-3': randint(1,6),
                'jogador-4': randint(1,6)}

ranking = []

print('Valores sorteados: ')
for k, v in jogadores.items():
    print(f'{k} tirou {v} no dado')

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('-'*30)
print('  == RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')

print('-'*30)
print('fim do programa')




