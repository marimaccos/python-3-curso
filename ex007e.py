# faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada

n = int(input('Digite um número para ver sua tabuada: '))
n0 = n * 0
n1 = n * 1
n2 = n * 2
n3 = n * 3
n4 = n * 4
n5 = n * 5
n6 = n * 6
n7 = n * 7
n8 = n * 8
n9 = n * 9


print('A tabuada desse número é:')
print('-' * 20)
print(n, 'x 0 =', n0)
print(n, 'x 1 =', n1)
print(n, 'x 2 =', n2)
print(n, 'x 3 =', n3)
print(n, 'x 4 =', n4)
print(n, 'x 5 =', n5)

# outro método / {:2} dois digitos para ficarem alinhados com os dois digitos do 10
print('{} x {:2} = {}'.format(n, 6, (n*6)))
print('{} x {:2} = {}'.format(n, 7, (n*7)))
print('{} x {:2} = {}'.format(n, 8, (n*8)))
print('{} x {:2} = {}'.format(n, 9, (n*9)))
print('{} x {:2} = {}'.format(n, 10, (n*10)))
print('-' * 20)

