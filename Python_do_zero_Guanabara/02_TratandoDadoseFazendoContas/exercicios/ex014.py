#Exercício Python 14: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

c = float(input('Informe a temperatura em ºC: '))
f = ((9 * c) / 5) + 32
print(f'A temperatura de {c}ºc corresponde a {f}ºf')