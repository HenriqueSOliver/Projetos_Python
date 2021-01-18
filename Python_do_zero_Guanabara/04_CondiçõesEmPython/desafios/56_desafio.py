#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

sidade = 0
midade = 0
mhomem = 0
nomevelho = ''
totmulher20 = 0

for c in range(0, 4):
    print(f'----- {c+1}º PESSOA -----')
    nome = str(input('Nome: ')).strip().upper()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    sidade += idade
    if c == 1 and sexo in 'Mm':
        mhomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > mhomem:
        mhomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
midade = sidade / 4
print(F'A média do grupo é de {midade:.0f} anos.')
print(f'O homem mais velho tem {mhomem} anos e se chama {nomevelho}')
print(f'Ao todo são {totmulher20} com menos de 20 anos.')
