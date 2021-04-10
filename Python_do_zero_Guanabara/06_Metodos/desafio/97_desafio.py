def tit(txt):
    tam = len(txt) + 4 # o tamanho será formatado de acordo com o tamanho do texto impresso
    print('~' * tam)
    print(f'  {txt}') #para centralizar o texto inicial apenas apliquei o f e 2 espaços
    print('~' * tam)


#Programa principal
tit('Olá Mundo')
tit('Sou Henrique')

