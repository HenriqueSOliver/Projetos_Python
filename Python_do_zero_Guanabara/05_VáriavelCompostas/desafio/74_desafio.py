
from random import randint

v = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Eu sorteei os valores : ', end='')
for n in v:
    print(f'{n} ', end='')
   
print(f'\nO menor valor digitado foi {min(v)}')
print(f'O maior valor digitado foi {max(v)}')

