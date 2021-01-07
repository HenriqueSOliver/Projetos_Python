#O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

n1 = str(input('Digite 1º nome '))
n2 = str(input('Digite 2º nome '))
n3 = str(input('Digite 3º nome '))
n4 = str(input('Digite 4º nome '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print(f'A ordem de apresentação será \n {(lista)}')