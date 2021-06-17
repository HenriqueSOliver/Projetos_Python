#help(input) #formato para consulta de help

#também temos ou formato de consulta
#print(input.__doc__) #imprimir o DOC Atributo do input tem informações diferente do Help

#DocStrings String de documentação, de um função que podemos criar por exemplo


def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela
    :para i: Inicio da contagem
    :para f: Fim da contagem
    :para p: Passo de contagem
    :return: sem retorno
    Função criada por Gustavo Guanabara (Aprendiz Henrique)
    """
    c = i
    while c <= f:
        print(f'{c}', end='..')
        c += p
    print('FIM !')

contador(2, 10, 2)

help(contador)

#parametro opcionais 
def somar(a=0, b=0, c=0):
    """
    -> Faz uma soma opcional
    :para a: primeira condição da soma (caso não informar valor vai aparecer 0)
    :para b: segundo condição da soma (caso não informar valor vai aparecer 0)
    :para c: terceiro condição da soma (caso não informar valor vai aparecer 0)
    :return: sem retorno
    Função criada por Gustavo Guanabara (Aprendiz Henrique)
    """
    s  = a + b + c
    print(f'A soma vale {s}')

somar(3, 2, 5) #1 teste 
somar(8, 4) # 2 teste
somar(c=3, a=2) #3  teste 
somar(b=3, c=1) #4 teste

# Escopo de Variáveis
def teste():
    x = 8 #variavel local
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')

#programa principal
n = 2 #variavel global
print(f'No programa principal, n vale {n}')
#teste()
#print(f'Na função teste, x vale {x}') # vai dar erro, pq X é uma variavel local

#Retorno de valores

def somar(a = 0, b = 0, c = 0):
    s = a + b + c
    return s

r1 = somar(3, 2, 1)
r2 = somar(1, 7)
r3 = somar(4)
print(f'Meus cálculos deram {r1} , {r2} e {r3}.')


#exercio para memorização

def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

n = int(input(f'Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')
#ou
#f1 = fatorial(5)
#f2 = fatorial(4)
#f3 = fatorial()
#print(f'Os resultados são {f1}, {f2} e {f3}')

#retornar verdadeiro ou falso

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('Não é par!')