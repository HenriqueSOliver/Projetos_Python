#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

print('='*30)
print(f'{"ANALISANDO UM TRIÂNGULO":^30}')
print('='*30)

n1 = int(input('Primeiro segmento: '))
n2 = int(input('Segundo segmento: '))
n3 = int(input('Terceiro segmento: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Os segmentos acima PODE FORMAR um Triângulo!')
else:
    print('Os segmentos NÃO PODEM FORMAR um triângulo!')