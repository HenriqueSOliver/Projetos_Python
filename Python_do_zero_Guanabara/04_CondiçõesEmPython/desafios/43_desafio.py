# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo: – IMC abaixo de 18,5: Abaixo do Peso – Entre 18,5 e 25: Peso Ideal – 25 até 30: Sobrepeso – 30 até 40: Obesidade  – Acima de 40: Obesidade Mórbida

print(f'='*30)
print(f'{"CALCULADORA DE IMC":^30}')
print(f'='*30)

p = float(input('Qual é o seu peso atual? '))
a = float(input('Qual é a sua altura? '))
imc = p / (a**a)
print(f'Seu IMC está em {imc:.1f} e você está', end=' ')
if imc < 18.5 :
    print('ABAIXO DO PESO')
elif imc < 25 :
    print('PESO IDEAL')
elif imc < 30 :
    print('SOBREPESO')
elif imc < 40 :
    print('OBESIDADE')
elif imc >= 40 :
    print('OBESIDADE MÓRBIDA')
else:
    print('[ERRO] DIGITE UM VALOR VÁLIDO')