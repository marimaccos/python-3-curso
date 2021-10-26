# crie um programa que leia um número real qualquer pelo teclado e
# mostre na tela sua porção inteira

from math import trunc

num = float(input('Digite um número real qualquer: '))

print('A porção inteira de {} é {}.'.format(num, trunc(num)))

# Método sem importação de módulo
print('A porção inteira de {} é {}.'.format(num, int(num)))
