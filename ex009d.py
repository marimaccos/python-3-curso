# crie um programa que leia o nome de uma pessoa e diga se ela tem 'Silva' no nome

nome = input('Digite seu nome: ').strip().title()

print('O nome digitado foi:', nome)
print('O nome tem Silva?', 'Silva' in nome)
