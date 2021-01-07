#Exercício Python 8: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

#primeiro modelo
medida = float(input('Uma distância em metros: '))
cm = medida * 100
mm = medida * 1000
print(f'A medida de {medida:.2f}m corresponde a {cm:.0f}cm e tantos {mm:.0f}mm')
