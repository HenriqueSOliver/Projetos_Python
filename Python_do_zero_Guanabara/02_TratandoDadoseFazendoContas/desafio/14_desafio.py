#Exercício Python 14: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.


c = float(input('Informe a temperatuda em ºC: '))
print(f'A temperatura de {c:.1f}ºc corresponde a {((9*c)/5)+32:.1f}ºf')