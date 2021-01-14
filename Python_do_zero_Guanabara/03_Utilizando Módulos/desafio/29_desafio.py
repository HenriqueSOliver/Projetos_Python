# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

print('~'*30)
print(f'{"RADAR ELETRÔNICO":^30}')
print('~'*30)

v = int(input('Qual é a sua velocidade atual do seu carro? '))
if v >= 81 :
    print(f'Você foi multado! e pagará R$ {(v-80)*7:.2f} pela sua infração!')
print('Tenha um bom dia! Dirija com segurança!')