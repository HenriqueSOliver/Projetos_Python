#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

print('='*30)
print(f'{"APROVADOR DE CRÉDITO":^30}')
print('='*30)

vi = float(input('Valor do imóvel? R$ ')) #vi valor imóvel
s = float(input('Salário do comprador? R$ '))
a = int(input('Quantos anos de financiamento? '))
viM = vi / (a * 12) # quantidade de meses
p = s * 30 / 100
print(f'Para pagar um imóvel de R$ {vi:.2f} em {a} anos a prestação será de R$ {viM:.2f}')
if p <= viM:
    print('Empréstimo NÃO pode ser aprovado!')
else:
    print('Empréstimo pode ser APROVADO!')
