lista = []

for cont in range(1,6):
    c = int(input(f'Digite o {cont}º valor: '))
    if cont == 0 or c lista[-1]:
        lista.append(c)
        print('Adicionado ao final da lista... ')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adiconado na posição {pos} da lista... ')

                break
            pos += 1


 
print(f'=-'*15)
print(f'Você digitou os valores {lista}')