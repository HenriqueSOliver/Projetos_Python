#faça um programa que leia o comprimento do cateto oposto e de cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa.
from math import hypot

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adijacente: '))
print(f'A hipotenusa vai medir {math.hypot(co, ca):.2f}')