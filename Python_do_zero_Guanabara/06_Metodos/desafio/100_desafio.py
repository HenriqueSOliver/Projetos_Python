from random import randint
from time import sleep

def sortLista(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for c in range (0, 5):
        n = randint(1,100)
        lista.append(n)
        print(f' {n}', end=' - ', flush=True)
        sleep(0.5)
    print('PRONTO')
        
def somaP(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')



#programa principal

números = []
sortLista(números)
somaP(números)

