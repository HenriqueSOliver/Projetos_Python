def tit(txt):
    tam = len(txt) + 4 # o tamanho será formatado de acordo com o tamanho do texto impresso
    print('~' * tam)
    print(txt)
    print('~' * tam)


#Programa principal
tit(f"{'Olá Mundo':^30}")
tit(f"{'Sou Henrique':^30}")

