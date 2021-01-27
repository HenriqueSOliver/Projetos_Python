

n = ('', '', '', '')

n = (int(input('Digite um número: ')),
int(input('Digite outro número: ')),
int(input('Digite mais um número: ')),
int(input('Digite o último número: ')))
print('-'*60)
print(f'Você digitou os números {n}')
if 9 in n:
    print(f'O valor 9 apareceu {n.count(9)} vezes')
else:
    print(f'O valor 9 não foi digitado')
if 3 in n:
    print(f'O número 3 apareceu na posição {n.index(3)}º')
else:
    print(f'O valor 3 não foi digitado')
for num in n:
    if num % 2 == 0:
        print(f'Os números pares que apareceram na tupla foram {num}')