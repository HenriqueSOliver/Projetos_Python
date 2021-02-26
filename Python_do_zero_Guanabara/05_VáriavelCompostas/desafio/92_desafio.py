from datetime import datetime


ficha = {}


print(F' === {"CASDASTRO DE TRABALHO":^30} ===')
ficha['Nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento [AAAA]: '))
ficha['Idade'] = datetime.now().year - nasc

ficha['Ctps'] = int(input('Nº CTPS - [0] não tem: '))
if ficha['Ctps'] != 0:
    ficha['Contratação'] = int(input('Ano de contratação [AAAA] :'))
    ficha['Salário'] = float(input('Salário atual: R$ '))
    ficha['Aposentadoria'] = ficha['Idade'] + ((ficha['Contratação'] + 35) - datetime.now().year)
print('-='*25)
for k, v in ficha.items():
    print(f'  - {k} tem o valor {v}')



