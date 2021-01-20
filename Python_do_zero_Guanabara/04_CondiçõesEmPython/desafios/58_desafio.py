# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

print(f'{"-"*100}')
print('Sou o seu computador')
print('Acabei de pensar em um número entre 0 e 10. Tente advinhar? ')
print(f'{"-"*100}')

pc = randint(0, 10)

s = 0
n = ''

while n != pc:
    n = int(input('Em que número eu pensei? '))
    s += 1
   
    if n < pc:    
        print('MAIS... Tente outra vez.')
        
    elif n > pc:
        print('MENOS... Tente outra vez.')
    
print(f'{"-"*100}')
print(f'Acertou com {s} tentativas. Parabéns!')
    


