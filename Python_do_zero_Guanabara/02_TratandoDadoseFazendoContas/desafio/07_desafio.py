#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média

nome = str(input('Digite o nome do aluno: '))
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
print(f"{nome} tirou {n1} na primeira prova e {n2} na segunda prova e a sua média foi {(n1+n2)/2:.2f}")