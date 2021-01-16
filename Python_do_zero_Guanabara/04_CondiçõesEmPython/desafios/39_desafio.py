# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

n = int(input('Em que ano você nasceu? '))
i = date.today().year - n
print(f'Quem nasceu em {n} tem {i} anos em {date.today().year}')
if i < 18 :
    print(f'Ainda faltam {18-i} anos para o alistamento.')
elif i == 18 :
    print(f'Você tem que se alistar IMEDIATAMENTE!')
else:
    resp = str(input('Você já se alistou [S] ou [N] ?')).upper()
    if resp == 'S':
        print(f'Parabéns você cumpriu o seu dever cívico')
    else:
        print(f'Você já deveria ter se alistado há {i-18} anos')
        print(f'Seu alistamento foi em {n+18}')
