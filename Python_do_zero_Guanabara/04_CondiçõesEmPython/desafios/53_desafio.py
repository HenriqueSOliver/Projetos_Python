#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:

#APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

f = str(input('Digite uma frase:  ')).upper().strip()
p = f.split()
juntar = ''.join(p)
inverso = ''
for c in range(len(juntar) -1, -1, -1):
    inverso += juntar[c]
print(f'O inverso de {juntar} é {inverso}')
if inverso == juntar:
    print('Temos um palíndromo! ')
else:
    print('A frase digitada não é palíndromo! ')



