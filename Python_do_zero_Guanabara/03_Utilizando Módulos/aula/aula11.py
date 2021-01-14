# como trabalhar com cores no terminal
#ANSI escape sequence (regulamentor de formatações)
# para cores no python, sempre utilizar \033[m
# \033[STYLO:TEXT:BACKGROUDm

#STYLO 0=nada 1=NEGRITO bold  4=sublinhado underline  7=Invertido negative

#TEXT 30=Branco 31=vermelhor 32= verde 33=amarelo 34=azulclaro 35=roxo 36=cian 37=cinza

#backgroud 40=fundobranco 41=fundovermelho 42=fundoverde 43=fundoamarelo 44=fundoazulclaro 45=fundoroxo 46=fundocian 47=fundocinza

print('\033[0;30;41mTESTE\033[m')
print('\033[4;33;44mTESTE\033[m')
print('\033[0;35;43mTESTE\033[m')
print('\033[1;30;42mTESTE\033[m')
print('\033[mTESTE\033[m')
print('\033[7;30mTESTE\033[m')

#mudar a cor de valores
n1 = int(input('Primeiro valor: '))
n2= int(input('Segundo valor'))
print(f'Os valores são \033[32m{n1}\033[m e \033[31m{n2}\033[m !')

#maneira mais avançada
nome = str(input('Qual é o seu nome? '))
print(f'Olá! Muito prazer em te conhecer, \033[m{nome}\033[m !!!')

#maneira mais avançada
nome = str(input('Qual é o seu nome? '))
#dicionário de cores
cores  = {'limpa':'\033[m', 'azul':'\033[34m', 'amarelo':'\033[33m', 'pretoebranco':'\033[7;30m'}

print(f'Olá! Muito prazer em te conhecer, {cores["amarelo"], nome, cores["limpa"]} !!!')