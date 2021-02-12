#faça um programa que leia 5 valores e coloque em uma lista

lista = []
maior = menor = 0

for cont in range(0,5):
    lista.append(int(input(f'Digite o {cont+1}º valor para posição {cont}: ')))
    if cont == 0:
        maior = menor = lista[cont]
    else:
        if lista[cont] > maior:
            maior = lista[cont]
        if lista[cont] < menor:
            menor = lista[cont]

print(f'=-'*50)
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {maior} nas posição ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}... ', end='')
print(f'\nO menor valor digitado foi {menor} nas posição ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}... ', end='')
