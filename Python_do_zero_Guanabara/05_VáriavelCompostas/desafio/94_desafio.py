
ficha = {}
fichat = []
soma = media = 0

while True:
    ficha.clear()
    ficha['Nome'] = str(input('Nome: ')).upper()
    while True:
        ficha['Sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if ficha['Sexo'] in 'MF':
            break
        print(f'[ERRO] - Por favor, digite apenas [M/F]: ')
    ficha['Idade'] = int(input('Idade: '))
    soma += ficha['Idade']


    fichat.append(ficha.copy())
    while True:
        r = str(input('Quer continuar ? [S/N]: ')).upper()[0]
        if r in 'SN':
            break
        print('[Erro] Responda apenas S ou N: ')
    if r == 'N':
        break

print('-='*25)
print(f' A) Ao todo temos {len(fichat)} pessoas cadastradas.')
media = soma / len(fichat)
print(f' B) A média de idade das pessoas cadastrasdas é de {media:5.2f} anos.')
print(f' C) As mulheres cadastradas foram ', end='')
for p in fichat:
    if p['Sexo'] == 'F':
        print(f'{p["Nome"]} ', end='/')
print()
print(f' D) Lista das pessoas que estão acima da média: ', end='')
for p in fichat:
    if p['Idade'] > media:
        print(f'  ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<<< ENCERRADO >>>')


