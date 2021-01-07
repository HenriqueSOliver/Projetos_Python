
#como trazer a biblioteca inteira e puxar após o ponto aumenta o consumo de memoria
import math

num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print(f'A raiz de {num} é igual a {raiz}')
print(f'A raiz de {num} é igual a {math.ceil(raiz)}')#formatação para arredondar o valor da raiz para cima
print(f'A raiz de {num} é igual a {math.floor(raiz)}')#formatação para arredondar o valor da raiz para baixo
print(f'A raiz de {num} é igual a {math.trunc(raiz)}')#formatação para trucar o valor


# como importar itens da biblioteca para economizar memoria

from math import sqrt, trunc
num = int(input('Digite um número: '))
raiz = sqrt(num)
print(f'A raiz de {num} é igual a {raiz}')


# importar random
import random
num = random.randint(1,10)
print(num)

# usar emoji
import emoji
print(emoji.emojize('Olá, mundo :sunglasses: ',use_aliases=True))