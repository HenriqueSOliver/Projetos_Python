#Exercício Python 5: Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor. escrito por Guanabara

#primeiro modelo
n = int(input('Digite um número: '))
a = n - 1
s = n + 1
print(f'Analisando o valor {n}, seu antecessor é {a} e o sucesso é {s}')

#segundo modelo
n = int(input('Digite um número: '))
print(f'Analisando o valor {n}, seu antecessor é {n-1} e o sucesso é {n-2}')