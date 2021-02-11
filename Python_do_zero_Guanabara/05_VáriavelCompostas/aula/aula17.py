# variáveis Compostas (listas) Parte I

#Lembrar Tuplas não permite alteração no dado informado - sempre colocamos () para tuplas
# Listas utilizamos o [] e pode ser alterado, e são mutais

lanche = ['pão', 'suco', 'pizza', 'pudim']
print(lanche) # vai mostrar toda lista
print(lanche[3]) # vai mostrar pudim
lanche[3] = 'sorvete' #o lanche 3 = pudim foi substituido para sorvete
print(lanche[3])
print(lanche)

#para adicionar itens na lista deve usar o comando .append('alguma coisa'), criar um novo elemento, será adicionado no final da lista
lanche.append('bolacha')
print(lanche)

#para adicionar itens em qualquer posição da lista, devemos usar o comando .insert, será adicionado na posição zero e os demais vão para direita e a minha lista passou a ter 0,1,2,3,4,5 espaços
lanche.insert(0,'HotDog')
print(lanche)

#remover pela chave
#para apagar elementos utilizando comando del e excluindo um espaço da lista deslocando a esquerda
del lanche[3]
print(lanche)

#remover pela chave
#também existe o comando pop geralmente ele é utilizado para apagar o ultimo elemento da lista, mas também podemos utilizar para apagar o elemento informando a posição
lanche.pop(3)
print(lanche)

#remover pelo conteudo
#tambem existe outro comando para excluir um item da lista, só que neste caso vamos indicar o item no lugar da posição exemplo 'pão'
lanche.remove('pão')
print(lanche)


#não tem como remover um elemento que não existe, caso realizar o comando direto vai dar erro.
#devemos que utilizar o comando if 'pizza' in lanche. (SE POR ACASO A PIZZA ESTIVER NA LISTA).
if 'pizza' in lanche:
    lanche.remove('pizza')

#também podemos utilizar um lista em range para fazer uma contagem de 4 até 10
#range cria uma lista ordenada, e forma crescente
valores = list(range(4,11))
print(valores)

#para fazer uma lista fora de ordem crescente
valores2 = [8, 2, 5, 4, 9, 3, 0]
print(valores2)

#como ordenar todos os valore de uma lista fora de ordem utilizamos o comando sort
valores2.sort()
print(valores2)

#como fazer a ordenação em ordem reversa utilizamos .sort(reverse=True)
valores2.sort(reverse=True)
print(valores2)

#Como sabemos o tamanho de uma lista utilizando o comando len, é muito utilizando em laços
len(valores2)

#Aula Prática
#num = (2, 5, 9, 1) #tupla
#num[2] = 3 não vai deixar alterar a tupla
#print(num)
num = [2, 5, 9, 1]
num[2] = 3 #alteri o valor do indice 2, neste caso 9 mudou para 3
num.append(7) # vamos incluir um novo valor na lista
print(num)
#teste se existe o número 4 para remover
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4')
print(num)
print(f'Essa lista tem {len(num)} elementos') # como mostrar os elementos utilizando len


#como iniciar uma nova lista com print bonito
valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for v in valores:
    print(f'{v}... ', end='')
print('FIM DA LISTA')

#como usar a chave + valor
valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores):
    print(f'Na posição {c} eu encontrei o valor {v}... ')
print('FIM DA LISTA')

#como incluir valores em uma lista
valores = []
for cont in range(0, 5):
    valores.append(int(input('Digite um número: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} eu encontrei o valor {v}... ')
print('FIM DA LISTA')

#como fazer uma cópia de uma lista, de uma forma q não altere as duas listas
a = [2, 3, 4, 7]
b = a[:] #utilizamos o fatiamento para criar uma cópia
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')