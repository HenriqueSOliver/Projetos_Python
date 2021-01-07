#faça um programa que leia um angulo qualquer e mostre na tela o valor de seno. cosseno e tangente desse angulo.

from math import radians, cos, tan, sin

a = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(a))
print(f'O ângulo de {a} tem o SENO de {seno:.2f}')
cosseno = cos(radians(a))
print(f'O ângulo de {a} tem o COSSENO de {cosseno:.2f}')
tangente = tan(radians(a))
print(f'O ângulo de {a} tem o TANGENTE de {tangente:.2f}')