#Escreva um programa que leia um valor em metros e converta em centimetros e milimetros.

m = float(input('Informe uma metragem: '))
print(f'A metragem informada convertida em centimetros é {m/10:.4f} e em milimetros ficaria {m/10000:.4f}')