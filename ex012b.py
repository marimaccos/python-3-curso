# Programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal, 3 para hexadecimal

num = int(input('Digite um número inteiro para fazer a conversão: '))
base = int(input('''Digite a opção da conversão
\033[31m1 - binário\033[m 
\033[32m2 - octal\033[m 
\033[34m3 - hexadecimal\033[m
Qual conversão desejada: '''))

if base == 1:
    print('{} para binário é igual a {}'.format(num, bin(num)[2:]))  #função com fatiamento para tirar os 2 primeiros digitos do número, retira os 0b,0o,0x

elif base == 2:
    print('{} para octal é igial a {}'.format(num, oct(num)[2:]))

elif base == 3:
    print('{} para hexadecimal é igual a {}'.format(num, hex(num)[2:]))

else:
    print('Erro!! Por favor, digite um número válido!')