# faça im programa que leia um ângulo qualquer e mostre na tela o valor do seno,
# cosseno e tangente desse ângulo

import math
print('Calculo do seno, cosseno e tangente.')

a = float(input('Digite o ângulo: '))

print('Seno: {:.2f}'.format(math.sin(math.radians(a))))
print('Cosseno: {:.2f}'.format(math.cos(math.radians(a))))
print('Tangente: {:.2f}'.format(math.tan(math.radians(a))))


