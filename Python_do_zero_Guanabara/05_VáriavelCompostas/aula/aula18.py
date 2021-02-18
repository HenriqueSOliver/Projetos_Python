teste = []
teste.append('Henrique')
teste.append(35)
galera = []
galera.append(teste[:])
teste[0] = 'Amanda' 
teste[1] = 33 
galera.append(teste[:])
print(galera)


galera2 = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera2[2][1]) # vai mostrar 13
print(' ')
for p in galera2: #para cada pessoa em galera > mostre pessoa 
    print(p)
print('Mostrar nome')
for p in galera2: # vai mostrar só os nomes
    print(p[0])
print('Mostrar só idade')
for p in galera2: # vai mostrar só os nomes
    print(p[1])
print('Formatado')
for p in galera2:
    print(f'{p[0]} tem {p[1]} de idade. ')


galera3 = []
dado = []
totmai = totmen = 0

for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera3.append(dado[:])#copia do dado
    dado.clear() #limpar o dado
print(galera3)
for p in galera3: # para cada pessoa em galera maior de 21 vamos printar
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade! ')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade! ')
        totmen += 1
print(f'Temos {totmai} maiores de idade e {totmen} menores de idade.')