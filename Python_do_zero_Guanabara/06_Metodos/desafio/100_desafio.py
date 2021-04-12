from random import randint

def sortLista(lista):
    for c in range (0, 5):
       lista.append(randint(1,100))
        


#programa principal

números = []
sortLista(números)
print(números)
