lista = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO',
        'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR',
        'MERCADO', 'FUTURO')

for p in lista:
    print(f'\n Na palavara {p} temos ', end='')
    for letra in p:
        if letra.upper() in 'AEIOU':
            print(letra, end=' ')





