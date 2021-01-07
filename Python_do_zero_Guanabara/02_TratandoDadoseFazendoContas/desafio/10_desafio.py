#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode compra
#considerando US$1,00 = R$ 3,27

r = float(input('Quanto reais você tem na sua carteira? R$ '))
d = float(input('Informe o valor do dolar? US$ '))
print(f'Com R$ {r}, você consegue comprar US$ {r/d:.2f}')