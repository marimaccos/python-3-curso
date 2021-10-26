# faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e
# todas as informações possiveis sobre ela

x = input('Digite algo: ')

print('Tipo:{}'.format(type(x)))
print('Numérico:{}'.format(x.isnumeric()))
print('Alpha:{}'.format(x.isalpha()))
print('Alphanumérico:{}'.format(x.isalnum()))
print('Maiuscula:{}'.format(x.isupper()))
print('Minuscula:{}'.format(x.islower()))
