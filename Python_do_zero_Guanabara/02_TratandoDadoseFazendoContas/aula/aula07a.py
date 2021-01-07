#Operadores aritméticos

# + adição 5 + 2 == 7
# - subtração 5 - 2 == 3 
# * multiplicação 5 * 2 == 10
# / divisão 5 / 2 == 2.5
# // divisão inteira 5 // 2 == 2
# ** potência 5 ** 2 == 25
# % resto da divisão 5 % 2 == 1

#Ordem de precedência
#1º ()
#2º **
#3º * / // % 
#4º + -

#exemplo
5+3*2
3*5+4**2
3*(5+4)**2

#como usar formatação alinhamento a 20 espaços a direita
nome = input('Qual é o seu nome? ')
print(f"Prazer em te conhecer {nome:>20}!")
#como usar formatação alinhamento a 20 espaços a esquerda
print(f"Prazer em te conhecer {nome:<20}!")
#como usar formatação alinhamento a 20 espaços a centralizado
print(f"Prazer em te conhecer {nome:^20}!")
#como usar formatação alinhamento a 20 espaços a centralizado mais sinais =
print(f"Prazer em te conhecer {nome:=^20}!")

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
print(f'A soma é {n1+n2}, o produto é {n1*n2} e a divisão é {n1/n2:.3f}', end=' ') #end para não quebrar a linha
print(f'Divisão inteira {n1//n2} \n e potência {n1**n2}') #quebrar linhas \n
