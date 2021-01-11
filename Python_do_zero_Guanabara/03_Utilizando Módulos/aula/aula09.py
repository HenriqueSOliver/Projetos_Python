# Nessa aula, vamos aprender operações com String no Python. As principais operações que vamos aprender são o Fatiamento de String, Análise com len(), count(), find(), transformações com replace(), upper(), lower(), capitalize(), title(), strip(), junção com join().

frase = 'Curso em Video Python'
print(frase[9]) #para mostrar o caracter alocado no 9 espaço V de video
print(20*'=')
print(frase[9:13]) #para mostrar o caracter alocado no 9 ao 13 Vide (Sempre exclui o ultimo espaço)
print(20*'=')
print(frase[9:21]) #para mostrar o caracter alocado no 9 ao 13 Video Python (Sempre exclui o ultimo espaço)
print(20*'=')
print(frase[9:21:2]) #para mostrar o caracter alocado no 9 ao 13 Video Python (Pulando de 2 em 2, ignorando o q estiver escrito na parte do pula)print(20*'=')
print(20*'=')
print(frase[:5]) #para mostrar o caracter alocado do inicio até o 4 (CURSO)
print(20*'=')
print(frase[15:]) #para mostrar o caracter alocado do espaço 15 até o final (utilizamos quando nao sabemos o total de caracteres) (PYTHON)
print(20*'=')
print(frase[9::3]) #para mostrar o caracter alocado do espaço 9 até o final, pulando 3 e 3


#como analisar uma string

print(20*'=')
print(len(frase)) #mostrar o comprimento de uma frase
print(20*'=')
print(frase.count('o')) #Contar quantas vezes tem a letra o
print(20*'=')
print(frase.count('o',0,13)) #Contar quantas vezes tem a letra o, com fatiamento 0 ao 12
print(20*'=')
print(frase.find('deo')) #encontrou onde inicia a palavara DEO, demonstrando em qual espaço
print(20*'=')
print(frase.find('Android')) #Vai demonstrar -1, pois não existe essa palavra na frase apontada
print(20*'=')
print('Curso' in frase) #Vai retornar se existe a palavra Curso na frase apontada, vai apresentar True 
print(20*'=')
print(frase.replace('Python', 'Android')) #Vai trocar a palavra python por Android 
print(20*'=')
print(frase.upper()) #Metodo que colocara td em maisculo
print(20*'=')
print(frase.lower()) #Metodo que colocara td em minusculo
print(20*'=')
print(frase.capitalize()) #Vai deixar somente a primeira em Maisculo o resto minusculo
print(20*'=')
print(frase.title()) #Toda letra após um espaço em braco ficará em maiusculo
outro = '    Aprenda Python   '
print(20*'=')
print(outro.strip()) #Vai remover os espaços em branco no inicio e no final do String 'xxxxAprenda Pythonxxx'
print(20*'=')
print(outro.rstrip()) #Vai remover os espaços no final da frase lado direito - String '    Aprenda Pythonxxx'
print(20*'=')
print(outro.lstrip()) #Vai remover os espaços inicio da frase lado esquerdo - String 'xxxxAprenda Python   '


#como dividir Strings


print(20*'=')
print(frase.split()) #VAi dividir os espaços que existem em uma frase / gerando uma nova lista para cada espaço
#Curso em Video Python
#01234567891011121314151617181920 total de espaços utilizados no frase
#Com split vamos dividir os espaços em branco ficando
#Curso em Video Python
#01234 01 01234 012345

print(20*'=')
print('-'.join(frase)) #vai colocar o sinal de - no espaços em branco


