#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.

i = soma = hsoma = fsoma = f = 0


while True:
    print(f'-'*60)
    print(f'{"CADASTRO UMA PESSOA":^60}')
    print(f'-'*60)

    i = int(input('Idade: '))
    if i >= 18:
        soma +=1

    s = ' '
    while s not in 'MF':
        s = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if s == 'M':
            hsoma +=1
        if s == 'F':
            fsoma +=1
        if i < 20 and s == 'F':
            f += 1

    print(f'-'*60)

    r = ' '
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break
    print(f'-'*60)
    
print(f'Total de pessoas com mais de 18 anos: {soma}')
print(f'Ao todo temos {hsoma} homens cadastrados')
print(f'E temos {fsoma} mulheres e {f} mulheres com menos de 20 anos.')
print('FIM DO PROGRAMA')





