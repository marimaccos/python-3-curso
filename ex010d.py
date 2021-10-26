# um programa que pergunte a distancia de uma viagem em km. calcule o preço da passagem, cobrando R$0.50 por km
# para viagens de ate 200km e R$0.45 para viagens mais longas

km = float(input('Qual a distância da viagem em km? '))

if km <= 200:
    print('A passagem para uma viagem de {}km sairá por R${:.2f}.'.format(km, km*0.50))

else:
    print('A passagem para uma viagem de {}km sairá por R${:.2f}.'.format(km, km*0.45))
