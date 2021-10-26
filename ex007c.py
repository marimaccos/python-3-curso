# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média

nome = input('Digite o nome do aluno: ')
n1 = float(input('Digite a primeira nota do aluno(a): '))
n2 = float(input('Digite a segunda nota do aluno(a): '))
m = (n1 + n2)/2

print('A média do aluno {} é: {:.1f}.'.format(nome, m))

