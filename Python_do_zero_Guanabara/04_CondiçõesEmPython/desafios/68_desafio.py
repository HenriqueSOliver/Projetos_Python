#Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

print('~'*80)
print(f'{"Vamos brincar de PAR ou ÍMPAR? ":^80}')
print('~'*80)

n = s = soma = par = impar = 0
op = v = s1 = ' '

while True:
    n = int(input('Digite um valor: '))
    pc = randint(0,10)
    s = n + pc
    if s % 2 == 0:
        s1 = 'PAR'
    else:
        s1 = 'ÍMPAR'
    op = str(input('Digite PAR ou ÍMPAR? [P/I]')).strip()[0].upper() 
    while op not in 'PI':
        op = str(input('[ERRO]-Digite um valor válido. PAR ou ÍMPAR? [P/I]')).strip()[0].upper()            
    print(f'Você jogou {n} e o computador {pc}. Resultando em {s} {s1}')
    if op == 'P':
        if n % 2 == 0:
            soma += 1
        else:
            break
    if op == 'I':
        if n % 2 == 1:
            soma += 1
        else:
            break
    print('VAMOS JOGAR NOVAMENTE ....')

if soma == 1:
    v = 'vez'
else:
    v = 'vezes'

print('~'*80)
print(f'GAME OVER! Você Venceu {soma} {v}.')






