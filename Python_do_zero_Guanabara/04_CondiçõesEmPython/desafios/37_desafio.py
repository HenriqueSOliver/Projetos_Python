#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

n = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ]-Converter para BINÁRIO
[ 2 ]-Converter para OCTAL
[ 3 ]-Converter para HEXADECIMAL''')
op = int(input('Informe a sua opção: '))
if op == 1:
    print(f'{n} convertido para BINÁRIO é igual {bin(n)}')
elif op == 2:
    print(f'{n} convertido para OCTAL é igual {oct(n)}')
elif op == 3: 
    print(f'{n} convertido para HEXADECIMAL é igual {hex(n)}')
else:
    print('[ERRO] digite um valor válido')