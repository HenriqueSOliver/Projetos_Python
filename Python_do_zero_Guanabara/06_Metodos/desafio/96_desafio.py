# cálcular área de um terro usando função

def area(l, c):
    m = l * c
    print(f'A área de um terreno {l:.2f} x {c:.2f} é de {m:.2f}m')
    


#PRINCIPAL
print(f'{"Controle de terreno":^30}')
print(f'-'*30)
l = float(input(f'LARGURA (m): '))
c = float(input(f'COMPRIMENTO (m): '))
area(l, c)
