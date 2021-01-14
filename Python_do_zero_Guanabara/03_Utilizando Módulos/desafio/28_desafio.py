#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

print('-'*100)
print('Vou pensar em um número Inteiro entre 0 e 5. Tente advinhar... ')
print('-'*100)

n = int(input('Em que número eu pensei? '))
if n == 2:
    print('Parabéns! ACERTOU')
else:
    print(f'GANHEI! eu pensei no número 2 e não {n}!')


from random import randint

pc = randint(0, 5)
print('-'*100)
print('Vou pensar em um número Inteiro entre 0 e 5. Tente advinhar... ')
print('-'*100)

n = int(input('Em que número eu pensei? '))
if n == pc:
    print('Parabéns! ACERTOU')
else:
    print(f'GANHEI! eu pensei no número {pc} e não {n}!')
