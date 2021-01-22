#Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

print(f'{"~"*30}')
print(f'{"10 TERMOS DE UMA PA":^30}')
print(f'{"~"*30}')

t = int(input('Primeiro termo: ')) #termo
r = int(input('Razão: ')) #razão vai pular de quantos em quantos
tf = t
c = 1
while c <= 10:
    print(f'{tf}', end=' -> ')
    tf += r
    c += 1
print('ACABOU')