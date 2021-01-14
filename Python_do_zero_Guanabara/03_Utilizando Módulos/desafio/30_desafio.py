#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

print('~'*80)
print(f'{"Vamos brincar de PAR ou ÍMPAR? ":^80}')
print('~'*80)

n = int(input('Diga um número qualquer: '))
if n % 2 == 0:
    print('PAR!')
else:
    print('ÍMPAR!')