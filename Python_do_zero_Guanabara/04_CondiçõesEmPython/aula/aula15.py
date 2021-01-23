# modelo anterior - Enquanto cont até 10 for verdade, será repetido
cont = 1 
while cont <= 10:
    print(cont, ' ...', end='')
    cont += 1
print('FIM')

# Usando o Enquanto VERDADE ele vai repetir para sempre, temos que colocar uma condição PARA=BREAK
n = s = 0 
while True:
    n = int(input('Digite um número: [Digite 999 para PARAR] '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}')