# crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
# considere US$1.00 = R$3.27

r = float(input("Digite quantos reais você possui: R$"))
d = r / 5.19
e = r / 5.79

print('Com R${:.2f}, você poderá comprar US${:.2f} e EUR${:.2f}.'.format(r, d, e))

