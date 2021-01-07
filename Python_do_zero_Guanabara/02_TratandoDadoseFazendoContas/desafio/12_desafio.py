#faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

print('LEITOR DE DESCONTO DE 5%')
vl = float(input('Informe o valor do produto: R$ '))
print(f'O produto ficará em R$ {vl-((vl*5)/100):.2f} com desconto de 5%')