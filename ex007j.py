# converter celsius em fahrenheit

c = float(input('Digite uma temperatura em C°: '))
f = c * 9 / 5 + 32

print('A temperatura de {}C° vale {:.1f}°F.'.format(c, f))
