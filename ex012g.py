# faça um programa que leia o comprimento de tres retas e diga ao usuario se elas podem ou nao formar um triangulo
# e qual triangulo formaria

print('\033[1;32mOlá, digite os valores das retas para saber se formará um triângulo e qual seria o tipo...\033[m')

a = int(input('Digite a primeira reta: '))
b = int(input('Digite a segunda reta: '))
c = int(input('Digite a terceira reta: '))

if b-c < a < b+c and a-c < b < a+c and a-b < c < a+b:
    print('Essas retas formam um triângulo...')

    from time import sleep
    sleep(2)

    if a == b == c:
        print('Equilátero!')

    elif a == b or b == c or a == c:
        print('Isósceles.')

    elif a != b != c:
        print('Escaleno')

else:
    print('Essas retas não formam um triângulo.')