# Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint

pc = randint(1, 3)
print(f'~'*30)
print(f'{"JO KEN PO":^30}')
print(f'~'*30)
r = int(input('''Escolha uma opção: 
[ 1 ] PAPEL
[ 2 ] PEDRA
[ 3 ] TESOURA
Qual é a sua jogada? '''))
print(f'~'*30)
if r == 1:
    print('Você jogou PAPEL')
elif r == 2:
    print('Você jogou PEDRA')
elif r == 3 :
    print('Você jogou TESOURA')

if pc == 1:
    print('Computador jogou PAPEL')
elif pc == 2:
    print('Computador jogou PEDRA')
elif pc == 3 :
    print('Computador jogou TESOURA')
else:
    print('[ERRO] - Digite um valor válido')

print(f'~'*30)

if r == pc :
    print('EMPATE! ')
elif r == 1 and pc == 2 or r == 2 and pc == 3 or r == 3 and pc == 1:
    print(f'JOGADOR VENCEU! ')
else:
    print('COMPUTADOR VENCEU')
