

n = c =  0

while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n <= 0:
        break
    print('-'*50)
    for c in range (0, 11):
        print(f'{n} x {c} = {n*c}')
        c +=1
    print('-'*50)
print(f'{"FIM DO PROGRAMA":^50}')