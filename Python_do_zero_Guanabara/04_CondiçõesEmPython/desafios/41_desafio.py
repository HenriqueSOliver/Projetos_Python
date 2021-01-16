# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade: – Até 9 anos: MIRIM  – Até 14 anos: INFANTIL  – Até 19 anos: JÚNIOR  – Até 25 anos: SÊNIOR  – Acima de 25 anos: MASTER

from datetime import date

a = int(input('Em que ano você nasceu? '))
i = date.today().year - a
print(f'O atleta tem {i} anos.')
if i >= 25 :
    print('Classificação: MASTER')
elif i >= 19 :
    print('Classificação: JÚNIOR')
elif i >= 14 :
    print('Classificação: INFANTIL')
else:
    print('Classificação: MIRIM')