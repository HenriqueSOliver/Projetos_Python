#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date

a = int(input('Que ano quer analisar? Coloque 0 para o ano atual: '))
if a == 0:
    a = date.today().year
if a % 4 == 0 and a % 100 != 100 or a % 400 == 0:
    print(f'O ano {a} é BISSEXTO!')
else:
    print(f'O ano {a} NÃO É BISSEXTO!')