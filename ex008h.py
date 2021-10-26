# o professor quer sortear a ordem de apresentação de trabalhos dos
# alunos. Faça um programa que leia o nome dos quatro alunos e mostre
# a ordem sorteada

# sample não repete elementos e pode ser escolhido um número específico de elementos
from random import sample

a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
lista = [a1, a2, a3, a4]

print('A ordem de apresentação será:', sample(lista, 4))
