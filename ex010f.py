# faça um programa que leia tres numeros e mostre qual é o maior e qual o menor

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))

if n1 > n2 and n1 > n3:
    print('O número {} é o maior'.format(n1))

if n2 > n1 and n2 > n3:
    print('O número {} é o maior'.format(n2))

if n3 > n1 and n3 > n2:
    print('O número {} é o maior'.format(n3))

if n1 < n2 and n1 < n3:
    print('O número {} é o menor'.format(n1))

if n2 < n1 and n2 < n3:
    print('O número {} é o menor'.format(n2))

if n3 < n1 and n3 < n2:
    print('O número {} é o menor'.format(n3))

