exp = str(input("Digite a sua expressão: "))
lista = []
for s in exp:
    if s == '(':
        lista.append('(')
    elif s == ')':
        if len(lista) > 0:
            lsita.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Sua expressão está válida! ')
else:
    print('Sua expressão está errada! ')