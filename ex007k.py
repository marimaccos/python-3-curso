# um programa que pergunte a quantidade de km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
# sabendo que o carro custa R$60/dia e R$0.15/km rodado.

km = float(input('Digite a quantidade de km percorridos: '))
dias = int(input('Digite a quantidade de dias alugado: '))
pg = (km * 0.15) + (dias * 60)

print('O total a pagar é R${:.2f}.'.format(pg))


