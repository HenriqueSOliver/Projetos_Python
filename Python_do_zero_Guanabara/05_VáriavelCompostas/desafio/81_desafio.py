lista = []


while True:
    lista.append(int(input('Digite um valor: ')))
    r = ' '
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break

print(f'*'*30)

print(f'Você digitou {len(lista)} valores')

lista.sort(reverse=True)
print(f'A lista em ordem decresente {lista}')

if 5 in lista:
    print(f'O número 5 está na lista na posição ')
else:
    print('Não achei o número 5')

print(f'*'*30)
print('FIM DO PROGRAMA')


