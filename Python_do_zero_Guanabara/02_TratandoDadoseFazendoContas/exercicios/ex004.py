#Como validar tipos primitivos
v = input('Digite um valor: ')
print(f'O tipo primitivo desse valor é {type(v)}')
print(f'Só tem espaços {v.isspace()}')
print(f'É um número? {v.isnumeric()}')
print(f'É alfabético? {v.isalpha()}')
print(f'É alfanumérico? {v.isalnum()}')
print(f'Está em maiúsculas? {v.isupper()}')
print(f'Está em minúsculas? {v.islower()}')
print(f'Está capitalizada? {v.istitle()}')

