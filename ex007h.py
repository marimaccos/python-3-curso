# faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto

pi = float(input('Digite o preço do produto: R$'))
pf = pi - (pi * 5 / 100)
# pf = pi * (1-0.05)

print('O produto que custava R${:.2f}, com desconto de 5% vai custar R${:.2f}'.format(pi, pf))
