#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
print('Validador de maior e menor')
print('~'*30)
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
if n1 > n2 and n1 > n3:
    print(f'O MAIOR valor digitado é {n1}')
if n2 > n1 and n2 > n3:
    print(f'O MAIOR valor digitado é {n2}')
if n3 > n1 and n3 > n2:
    print(f'O MAIOR valor digitado é {n3}')
if n1 < n2 and n1 < n3:
    print(f'O MENOR valor digitado é {n1}')
if n2 < n1 and n2 < n3:
    print(f'O MENOR valor digitado é {n2}')
if n3 < n1 and n3 < n2:
    print(f'O MENOR valor digitado é {n3}')



