#Nessa aula, vamos aprender como utilizar estruturas condicionais simples e compostas nos seus programas em Python.

tempo = int(input('Quantos anos tem o seu carro? '))
if tempo <= 3:
    print('Carro Novo!')
else:
    print('Carro velho!')
print('--FIM--')

#condição simplificada
tempo = int(input('Quantos anos tem o seu carro? '))
print('Carro Novo! ' if tempo <= 3 else 'Carro velho!')
print('--FIM--')

#pratica
n = str(input('Qual é o seu nome? ')).title()
if n == 'Henrique':
    print('Que nome lindo que você tem!')    
print(f'Bom dia, {n}')

n = str(input('Qual é o seu nome? ')).title()
if n == 'Henrique':
    print('Que nome lindo que você tem!')
else:
    print('Seu nome é tão normal!') 
print(f'Bom dia, {n}')


n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite outra nota: '))
m = (n1 + n2) / 2
print(f'A sua média foi {m:.1f}')
if m >= 6.0:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('A média foi ruim! REPROVADO!')