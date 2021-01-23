#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

n = s = c = maiorv = menorv = 0

resp = 'S'
while resp in 'S':
    n = int(input('Digite um valor: '))
    resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    s += n
    c += 1
    if n == 1 :
        maiorv = menorv = n
    else:
        if n > maiorv:
            maiorv = n
        if n < menorv:
            menorv = n

m = s / c
print(f'A soma dos valores digitado foi {s} e a média do valores digitados foi {m:.2f}')
print(f'O maior valor digitado foi {maiorv} e o menor valor foi {menorv}')


