
lista = []

while True:
    val = int(input('Digite um valor: '))
    
    if val not in lista:
        lista.append(val)
    else:
        print('Valor duplicado! Não vou adicionar na lista')

    r = ' '
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break

print(f'*'*30)
print('FIM DO PROGRAMA')
lista.sort()
print(lista)
