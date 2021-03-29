#Nessa aula, vamos aprender o que são funções ou rotinas e como utilizar funções em Python. Funções são trechos de código que podem ser executados em momentos diferentes de nossos códigos em Python. Veja como funciona o comando def em Python e como utilizá-lo com parâmetros simples e múltiplos.

#TEORIA 
#------------------------------------------------------
def lin(): #lin = linha
    print('-'*30)


#PROGRAMA PRINCIPAL 
lin()
print(f"{'CURSO EM VIDEO':^30}")
lin()
print(f"{'APRENDA PYTHON':^30}")
lin()
print(f"{'PROF GUSTAVO GUANABARA':^30}")
lin()


def título(txt):
    print('-'*30)
    print(txt)
    print('-'*30)


#PROGRAMA PRINCIPAL
título(f"{'APRENDER É PRATICAR':^30}")
título(f"{'PYTHON É MUITO BOM!':^30}")
título(f"{'HENRIQUE S OLIVEIRA':^30}")

#------------------------------------------------------

#PRÁTICA 1
#------------------------------------------------------
def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')
    print('-'*30)


#PROGRAMA PRINCIPAL
soma(4, 5)
soma(8, 9)
soma(b=2, a=1) # posso trocar a ordem para mostrar os números

#PRÁTICA 2
#------------------------------------------------------
def contador(*núm):
    for valor in núm:
        print(f'{valor} ', end='')
    print('> FIM!')

#PROGRAMA PRINCIPAL
contador(5, 7, 3, 1, 4)
contador(8, 4, 7)
contador(4, 4, 7, 6, 2, 10, 20, 35)

#PRÁTICA 3
#------------------------------------------------------
def contador(*núm):
    tam = len(núm)
    print(f'Recebi os valores {núm} e são ao todo {tam} números')

#PROGRAMA PRINCIPAL
contador(5, 7, 3, 1, 4)
contador(8, 4, 7)
contador(4, 4, 7, 6, 2, 10, 20, 35)

#PRÁTICA 4
#------------------------------------------------------
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


#PROGRAMA PRINCIPAL
valores = [50, 60, 65, 70, 75, 80, 100]
dobra(valores)
print(valores)