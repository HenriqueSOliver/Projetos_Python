#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

km = float(input('Qual é a distância da sua viagem? '))
print(f'Você está prestes a começar uma viagem de {km:.1f}Km')
if km <= 200:
    print(f'E o preço da sua passagem será de R$ {km*0.50:.2f}')
else:
    print(f'E o preço da sua passagem será de R$ {km*0.45:.2f}')
print('Tenha uma boa viagem!')