from random import randint
jogada = []
njogada = []

print('-'*50)
print(f'{"JOGO NA MEGA SENA":^50}')
print('-'*50)
c = int(input('Quantos jogos você quer que eu sorteie? '))

t = 1
while t <= c:
    cont = 0
    while True:
        j = randint(1, 60)
        if j not in jogada:
            jogada.append(j)
            cont += 1
        if cont >= 6:
            break
    jogada.sort()
    njogada.append(jogada[:])
    jogada.clear()
    t += 1
        
print('-='*9, f' SORTEANDO {j} JOGOS', '-='*9)
for i, l in enumerate(njogada):
    print(f'Jogo {i+1}: {l}')

print(f'-='*10, end=' ')
print(f'< BOA SORTE! >',end='')
print('-='*9)