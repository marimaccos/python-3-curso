# programa que leia dois números inteiros e compare-os, mostrando:
# o primeiro valor é maior / o segundo valor é maior / não existe valor maior, os dois são iguais

from time import sleep

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

print('Carregando...')
sleep(3)

if n1 > n2:
    print('O número {} é maior que o número {}'.format(n1, n2))

elif n2 > n1:
    print('O número {} é maior que o número {}'.format(n2, n1))

else:
    print('Não existe maior, os dois são iguais.')