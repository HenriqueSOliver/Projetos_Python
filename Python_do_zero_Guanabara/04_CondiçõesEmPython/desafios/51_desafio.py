#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

print(f'{"~"*30}')
print(f'{"10 TERMOS DE UMA PA":^30}')
print(f'{"~"*30}')

t = int(input('Primeiro termo: ')) #termo
r = int(input('Razão: ')) #razão vai pular de quantos em quantos
d = t + (10 - 1) * r
for c in range(t, d + r, r):
    print(f'{c}', end=' -> ')
print('ACABOU')