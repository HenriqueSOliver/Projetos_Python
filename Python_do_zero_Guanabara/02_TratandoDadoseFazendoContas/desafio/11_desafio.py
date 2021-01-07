#faça um programa que leia largura e altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pinta-la, sabendo que cada litro de tinta pintada área de 2m.

print('Calcular metragem para pintura')
a = float(input('Qual é a altura da sua parede: '))
l = float(input('Qual é a largura da sua parede: '))
print(f'A área quadrada da sua parede é de {a*l:.2f}M e você precisará de {(a*l)/2:.2f} Litros de tinta')