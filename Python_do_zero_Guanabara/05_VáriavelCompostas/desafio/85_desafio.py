num = [[], []]
val = 0


for cont in range (0,7):
    val = int(input(f'Digite o {cont+1}º valor: '))
    if val % 2 == 0:
        num[0].append(val)
    else:
        num[1].append(val)

num[0].sort()
num[1].sort()

print('=' * 30)
print(f'Você digitou os valores {num}')
print(f'Desta lista os números {num[0]} são pares')
print(f'E os valores {num[1]} são impares')