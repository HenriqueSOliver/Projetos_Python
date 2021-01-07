#Exercício Python 7: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.  

#primeiro modelo
n1 = float(input('Primeiro nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
m = (n1+n2)/2
print(f'A média entre {n1} e {n2} é igual {m}')

#Segundo modelo
n1 = float(input('Primeiro nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
print(f'A média entre {n1} e {n2} é igual {(n1+n2)/2:.1f}')