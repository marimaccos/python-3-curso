# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiza quadrada

n = int(input('Digite um número: '))
d = n*2
t = n*3
r = n**(1/2)

print('Seu número foi:', n)
print('Seu dobro é {}, seu triplo é {} e sua raiz é {:.2f}.'.format(d, t, r))
