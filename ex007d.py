# escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

m = float(input('Digite um valor em metros: '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000

print('{:.3f} km\n{:.3f} hm\n{:.3f} dam\n{} m\n{} cm\n{} mm'.format(km, hm, dam, m, cm, mm))


