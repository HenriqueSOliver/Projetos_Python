lista = []
pares = []
impar = []

while True:
    lista.append(int(input('Digite um valor: ')))
    r = ' '
    while r not in 'SN':
        r = str(input('Deseja Continuar? [S/N]: ')).strip().upper()[0]
    if r == 'N':
        break

print('-='*30)

print(f'Você digitou os valore {lista}')

for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    else:
        impar.append(v)

print('-='*30)

print(f'Lista PAR {pares}')
print(f'Lista IMPARES {impar}')

print('-='*30)
print('FIM DO PROGRAMA')