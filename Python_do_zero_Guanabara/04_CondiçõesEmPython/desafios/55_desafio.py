#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

print(f'{"="*30}')
print(f'{"Analisador de peso":^30}')
print(f'{"="*30}')

pmaior = 0
pmenor = 0


n = int(input('Quer analisar o peso de quantas pessoas? '))

for c in range(0, n):
    p = float(input(f'Peso da {c+1}º pessoa: '))
    if c == 1:
        pmaior = p
        pmenor = p
    else:
        if p > pmaior:
            pmaior = p
        if p < pmenor:
            pmenor = p
print(f'O maior peso foi {pmaior}')
print(f'O menor peso foi {pmenor}')
