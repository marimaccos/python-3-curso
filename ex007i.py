# faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento

si = float(input('Digite seu salário: R$'))
sf = si + (si * 15 / 100)
# sf = si * (1 + 0.15)

print('Seu salário era R${}, com aumento de 15% seu novo salário será: R${:.2f}.'.format(si, sf))
