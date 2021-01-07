# validando formato float, digito um número 4 e vai apresentar 4.0
n = float(input('Digite um valor: '))
print(n)

#como inserir um texto e se podemos transformar em numero, true ou false
n1 = input('Digite algo: ')
print(n1.isnumeric())

# como validar se é letra
n2 = input('Digite outra coisa: ')
print(n2.isalpha())

#como validar se é alfa numerico
n3 = input('Outra coisa: ')
print(n3.isalnum())