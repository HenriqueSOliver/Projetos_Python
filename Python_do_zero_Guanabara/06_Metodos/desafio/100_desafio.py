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
        


#programa principal

números = []
sortLista(números)

