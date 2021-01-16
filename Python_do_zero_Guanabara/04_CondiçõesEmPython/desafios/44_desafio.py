# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento: 
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal 
# – 3x ou mais no cartão: 20% de juros

print(f'{"~"*10} LOJINHA DO HENRIQUE {"~"*10}')
cp = float(input('Preço das compras: R$ '))
r = int(input('''FORMA DE PAGAMENTO 
[ 1 ] À vista dinheiro/cheque
[ 2 ] À vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
Qual é a sua opção?'''))
if r == 1 :
    print(f'Sua compra de R$ {cp:.2f} vai custar R$ {cp-(cp*10/100):.2f} com desconto de 10%')
elif r == 2 :
    print(f'Sua compra de R$ {cp:.2f} vai custar R$ {cp-(cp*5/100):.2f} com desconto de 5%')
elif r == 3 :
    print(f'Sua compra de R$ {cp:.2f} parcelada em 2x ficará em R${cp/2}ao mês ')
elif r == 4 :
    j = cp + (cp * 20 / 100)
    v = int(input('Quantas vezes gostaria de parcelar? '))
    print(f'Sua compra de R$ {cp:.2f} parcelado em {v}x ficará em R$ {j / v:.2f}')


