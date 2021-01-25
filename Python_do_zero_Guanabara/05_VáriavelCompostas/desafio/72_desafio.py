n = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'donze', 'treze', 'quartorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

r = ''
while True:
    r = int(input('Digite um número entre 0 e 20: '))
    if 0 <= r <= 20:
        break
    print('Tente novamente. ', end='')
print(f'Você digitou o número {n[r]}')