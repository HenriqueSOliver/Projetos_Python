# contar de 0 até 6
for c in range(0, 7):
    print(c)
print('FIM')

# contar de 0 até 6, pulando de 2 em dois
for c in range(0, 7, 2):
    print(c)
print('FIM')

# definir a contagem até um determinado numero escolhido pelo usuário
n = int(input('Digite um número: '))
for c in range (0, n+1):
    print(c)
print('FIM')

#  definir a contagem inicial, final e pular até um determinado numero escolhido pelo usuário,
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range (i, f+1, p):
    print(c)
print('FIM')

#Como aplicar um for para leitura de uma número apontado pelo usuário
for c in range(0, 3):
    n = int(input('Digite um valor: '))
print('FIM')


#Como aplicar um for para leitura de uma número apontado pelo usuário + somando os valores
s = 0
for c in range(0, 3):
    n = int(input('Digite um valor: '))
    s += n
print(f'O somatório de todos os valores foi {s}')
print('FIM')

