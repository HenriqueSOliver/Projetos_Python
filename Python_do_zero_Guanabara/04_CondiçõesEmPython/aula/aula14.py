
# modelos de estrutura de repetição

#FOR vai contar de 1 até 9 - só posso usar quando sei o limite
for c in range (1, 10):
    print(c)
print('FIM')

#posso usar o  while também quando sei o limite
c = 1
while c < 10:
    print(c)
    c += 1
print('FIM')

# com condição de parada
n = 1
while n != 0:
    n = int(input('Digite um valor - aperte[0] parar'))
print('FIM')

r = 'S'
while r in 'Ss':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] '))
print('FIm')

n = 1 
par = impar = 0
while n !=0:
    n = int(input('Digite um valor: '))
    if n != 0:    
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'você digitou {par} números pares e {impar} números ímpares.')