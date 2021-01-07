# crie um prograa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.

from math import trunc

n = float(input('Digite um número real: '))
print(f'O número {n} tem a parte inteira {trunc(n)}')

#ou
n = float(input('Digite um número real: '))
print(f'O número {n} tem a parte inteira {int(n)}')