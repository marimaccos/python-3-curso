# programa que leia a velocidade de um carro. se ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# a multa vai custar R$7.00 por cada km acima do limite

vel = float(input('Velocidade em km/h registrada: '))


if vel > 80:
    print('Você foi multado! Deverá pagar R${:.2f} de multa'.format((vel - 80)*7))

else:
    print('Velocidade dentro do permitido!')
