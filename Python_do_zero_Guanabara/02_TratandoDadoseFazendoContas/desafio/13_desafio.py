#faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

print('Atualização salárial de 15%')
s = float(input('Informe o salário atual: R$ '))
print(f'O salário informado foi reajustado em 15% e ficará em R$ {s+((s*15)/100):.2f}')