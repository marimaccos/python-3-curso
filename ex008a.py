# importando funcionalidades específicas

from math import sqrt, pow

num = int(input('Digite um número: '))
raiz = sqrt(num)
pot = pow(num, 2)

print('A raiz de {} é {:.2f}'.format(num, raiz))
print('A potência de {} é {:.2f}'.format(num, pot))
