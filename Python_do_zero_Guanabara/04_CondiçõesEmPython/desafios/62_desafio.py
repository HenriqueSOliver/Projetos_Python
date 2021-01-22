#Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

print(f'{"~"*30}')
print(f'{"10 TERMOS DE UMA PA":^30}')
print(f'{"~"*30}')

t = int(input('Primeiro termo: ')) #termo
r = int(input('Razão: ')) #razão vai pular de quantos em quantos
tf = t
c = 1
while r != 0:
    while c <= 10:
        print(f'{tf}', end=' -> ')
        tf += r
        c += 1
    print('PAUSA')
    r = int(input('Quantos termos você quer mostrar a mais? '))
print('ACABOU')