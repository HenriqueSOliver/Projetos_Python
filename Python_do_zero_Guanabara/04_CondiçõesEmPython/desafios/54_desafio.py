#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

totmaior = 0
totmenor = 0

n = int(input('Quer analisar quantas pessoas? '))
atual = date.today().year
for c in range(0,n):
    a = int(input(f'Em que ano a {c+1}º pessoa nasceu? '))
    i = atual - a
    if i >= 21:
        totmaior +=1
    else:
        totmenor +=1
print(f'Ao todo tivemos {totmaior} pessoas maiore de idade')
print(f'E também tivemos {totmenor} pessoas menores de idade')