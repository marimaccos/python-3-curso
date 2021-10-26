# faça um programa que leia o comprimento do cateto oposto e do
# cateto adjacente de um triângulo retângulo, calcule e mostre o
# comprimento da hipotenusa

from math import sqrt, pow

co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
h = sqrt(pow(co, 2)+pow(ca, 2))

# Sem importar módulos
#h = (co**2 + ca**2) ** (1/2)

print('O comprimento da hipotenusa é igual a {:.2f}'.format(h))

