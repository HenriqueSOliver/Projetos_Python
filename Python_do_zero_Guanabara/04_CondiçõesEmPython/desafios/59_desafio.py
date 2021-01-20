#Crie um programa que leia dois valores e mostre um menu na tela: 
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.

c = 0
r = ''

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

while r != 5:
    r = int(input('''[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do programa
>>>>> Qual é a sua opção? '''))
    if r == 1:
        c = n1 + n2
        print(f'A soma entre {n1} + {n2} é {c}')
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    elif r == 2: 
        c = n1 * n2
        print(f'A Multiplicação entre {n1} x {n2} é {c}')
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    elif r == 3:
        if n1 > n2:
            c == n1
            print(f'{n1} é MAIOR que {n2}')
            print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        elif n1 == n2:
            c == n1
            print(f'{n1} e {n2} são IGUAIS')
            print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        else:
            c == n2
            print(f'{n2} é MAIOR que {n1}')
            print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    elif r == 4 :
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif r == 5 :
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        print('Finalizando ....')
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    else:
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        print('[ERRO] - Opção inválida. Tente Novamente')






