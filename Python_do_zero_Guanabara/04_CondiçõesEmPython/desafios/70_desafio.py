#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

total = prot = pre = c = mpre = 0
npro = pro = ''

while True:
    print(f'-'*60)
    print(f'{"LOJA DE TRECOS":^60}')
    print(f'-'*60)

    
    pro = str(input('Nome do Produto: ')).strip().upper()
    pre = int(input('Preço: R$ '))
    c += 1
    total += pre
    if pre >= 1000:
        prot += 1
    if c == 1 or pre < mpre:
        mpre = pre
        npro = pro
    r = ' '
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break

print(f'-'*60)
print(f"{'FIM DO PROGRAMA':^60}")
print(f'O total da compra foi R$ {total:.2f}')
print(f'Temos {prot} custando mais de R$ 1.000,00')
print(f'O produto mais barato foi {npro} que custa R$ {mpre:.2f}')
