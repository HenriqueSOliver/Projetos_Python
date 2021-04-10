#Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def m(* núm):
    cont = m = 0
    print(f'Analisando os valores passados... ')
    for valor in núm:
        print(f'{valor} ', end='')
        if cont == 0 :
            m = valor
        else:
            if valor > m:
                m = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {m}')
    print('~'*30)
    print('')



#PROGRAMA PRINCIPAL
m(5, 7, 3, 1, 4)
m(8, 4, 7)
m(4, 4, 7, 6, 2, 10, 20, 35)
m(0)