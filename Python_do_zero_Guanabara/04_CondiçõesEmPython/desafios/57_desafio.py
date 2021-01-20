# criar um programa que leia o sexo de uma pessoa, mas só aceita os valores 'M' ou 'F'. caso esteja errado, peça a digitação novamente até ter um valor correto.


sexo = str(input('Digite o seu sexo [M/F]: ')).strip().upper()[0] #tirar os espaços e pegar a primeira letra
while sexo not in 'MF':
    sexo = str(input('[ERRO]-Dados inválidos. Por favor digite o seu sexo [M/F]: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso.')
print('FIM')


