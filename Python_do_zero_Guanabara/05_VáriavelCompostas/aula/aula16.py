# Váriavel COMPOSTOS TUPLAS

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche)
print(lanche[1])
print(lanche[-2]) # vai pegar o segundo elemento de tras pra frente
print(lanche[1:3])# vai mostrar uma parte da tupla = 1 e 2
print(lanche[2:])# vai mostrar os elentos do dois até o final
print(lanche[:2])# vai mostrar os elementos 0 e 1, não vai mostrar o elemento 2
print(lanche[-2:])# vai começar a mostra o elemento 2 até o final
# TUPLAS SÃO IMUTÁVEIS

#vai mostrar a tupla repetindo a frase e mostrando apenas um elemento por vez, subistituindo o anterior
lanche2 = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
for comida in lanche2:
    print(f'Eu vou comer {comida}')
print(f'Comi pra caramba!')

#vai mostrar 4 elementos
lanche2 = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(len(lanche2))

#usando o range vamos mostros os itens
lanche2 = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
for cont in range (lanche2[cont]):
    print(f'Eu vou comer {lanche2[cont]}')
print(f'Comi pra caramba!')

#usando o range permite mostrar a posição do elemento
lanche2 = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
for cont in range (lanche2[cont]):
    print(f'Eu vou comer {lanche2[cont]} na posição {cont}')
print(f'Comi pra caramba!')
print('-'*30)


#usando enumerate para numerar os elementos
lanche2 = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
for pos, comida in enumerate lanche2:
    print(f'Eu vou comer {comida} na posião {pos}')
print(f'Comi pra caramba!')
print('-'*30)

#mostar os elementos em ordem Alfabética 
lanche2 = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(sorted(lanche2))
print('-'*30)

#criar 2 tuplas com elementos diferente e juntar
a = (2, 5 , 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(len(c))#vai mostrar quantos elementos na tupla
print(c.count(5)) # quantas vezes apareceu o numero 5, neste caso 2 vezes
print(c.index(8)) # em que posição está o 8 que neste caso é o 4
print(c.inde(5, 1))# vai mostrar a posição do 5 apos a primeira vez. Indez não permite mostrar mais de uma vez
print('-'*30)

# dentro da tupla podemos ter ambos dados STR ou INT, FLOAT
pessoa = ('Henrique', 35, 'M', 70.78)
print(pessoa)
print('-'*30)

# MAPAR APAGAR A TUPLA, del vai aparecer msg de tupla apagada
#pessoa = ('Henrique', 35, 'M', 70.78)
#del(pessoa)
#print(pessoa)
#print('-'*30)

