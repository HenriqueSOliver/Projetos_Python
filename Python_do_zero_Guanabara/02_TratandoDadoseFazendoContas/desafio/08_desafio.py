#Escreva um programa que leia um valor em metros e converta em centimetros e milimetros.

m = float(input('Informe uma metragem: '))
print(f'A metragem informada convertida em centimetros é {m*100:.2f}cm e em milimetros ficaria {m*1000:.0f}mm')