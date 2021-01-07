#Exercício Python 11: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
print(f'Sua parede tem a dimensão de {larg} x {alt} e a sua área é de {area:.1f}m')
tinta = area / 2
print(f'Para pintar essa parede, você precisará de {tinta:.1f}l de tinta.')