#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

n = str(input('Digite o seu nome completo: ')).capitalize().strip().split()
print(f'Muito prazer em te conhecer {n[0]}')
print(f'Seu primeiro nome é {n[0]}')
print(f'Seu último nome é {n[len(n)-1]}')