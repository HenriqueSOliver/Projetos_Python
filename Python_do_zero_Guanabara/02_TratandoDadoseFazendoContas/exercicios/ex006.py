#Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada. script Guanabara

#primeiro modelo
n = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = n **(1/2)
print(f'O dobro de {n} vale {d}')
print(f'O triplo de {n} vale {t}')
print(f'A Raiz quadrada de {n} é igual {r:.2f}')

#segundo modelo
n = int(input('Digite um número: '))
print(f'O dobro de {n} vale {n*2}')
print(f'O triplo de {n} vale {n*3}')
print(f'A Raiz quadrada de {n} é igual {n**(1/2):.2f}')

