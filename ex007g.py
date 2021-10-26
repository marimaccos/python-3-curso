# faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2m²

l = float(input('Digite a largura em metros: '))
h = float(input('Digite a altura em metros: '))
a = l * h
q = a / 2

print('A área a ser pintada será: {:.2f}m²'.format(a))
print('A quantidade de tinta necessária será: {:.2f} litros'.format(q))
