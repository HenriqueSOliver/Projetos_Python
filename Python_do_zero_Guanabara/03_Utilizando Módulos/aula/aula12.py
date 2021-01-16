# Laço de Repetição FOR

#laço contador no intervalo (1,10): 
#for c in range(0,3):
    #if moeda :
        #pega
    #passo
    #pula
#passo
#pega

for c in range(1, 7):
    print(c'Oi')
print('FIM')

# -1 é a iteração
for c in range(6, 0, -1):
    print(c'tchau')
print('FIM')
 
#contar puldando 2 em 2
for c in range(0, 7, 2):
    print(c)
print('FIM')


n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)
print('FIM')

i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')

for c in range(0, 3):
    n = int(input(f'Digite {c}º número: '))
print('FIM')

s = 0
for c in range(0, 3):
    n = int(input(f'Digite {c}º número: '))
    s += n
print(f'O somatório de todos os valores foi {s}')