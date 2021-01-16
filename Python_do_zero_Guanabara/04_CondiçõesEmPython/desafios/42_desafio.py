#Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado: – EQUILÁTERO: todos os lados iguais  – ISÓSCELES: dois lados iguais, um diferente  – ESCALENO: todos os lados diferentes


print('='*30)
print(f'{"ANALISANDO UM TRIÂNGULO":^30}')
print('='*30)

n1 = int(input('Primeiro segmento: '))
n2 = int(input('Segundo segmento: '))
n3 = int(input('Terceiro segmento: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Os segmentos acima PODE FORMAR um Triângulo ', end='')
    if n1 == n2  == n3 :
        print('EQUIlÁTERO')
    elif n1 != n2 != n3 != n1 :
        print('ESCALENO') 
    else:
        print('ISÓSCELES')
else:
    print('Os segmentos NÃO PODEM FORMAR um triângulo!')