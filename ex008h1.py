# shuffle embaralha os elementos da lista
from random import shuffle

a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
lista = [a1, a2, a3, a4]

# a função shuffle tem que vir antes do print
shuffle(lista)
print('A ordem de apresentação será:', lista)

shuffle(lista)
print(lista)

shuffle(lista)
print(lista)
