# faça um programa que leia o comprimento de tres retas e diga ao usuario se elas podem ou nao formar um triangulo

a = float(input('Digite o comprimento da reta 1: '))
b = float(input('Digite o comprimento da reta 2: '))
c = float(input('Digite o comprimento da reta 3: '))

if (b-c) < a < b+c and (a-c) < b < a+c and (a-b) < c < a+b:
    print('As retas formam um triângulo.')

else:
    print('As retas não formam um triângulo.')


