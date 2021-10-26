# faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e
# todas as informações possiveis sobre ela

x = input('Digite algo: ')

print('O que você digitou foi: ', x)

print('O tipo primitivo desse valor é: ', type(x))
print('É um numéro? ', x.isnumeric())
print('Só tem espaços? ', x.isspace())
print('É alfabético? ', x.isalpha())
print('É alfanumérico? ', x.isalnum())
print('Está em maiúsculas? ', x.isupper())
print('Está em minúsculas? ', x.islower())
print('Está capitalizado? ', x.istitle())

