# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
if n1 < n2:
    print(f'{n1} é MENOR que {n2}')
elif n1 > n2:
    print(f'{n1} é MAIOR que {n2}')
else:
    print(f'{n1} é IGUAL à {n2}')