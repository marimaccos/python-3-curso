# importando o módulo random, classes random e randint

import random

n1 = random.randint(1, 50) #radomiza um numero inteiro no intervalo solicitado
n2 = random.random() #randomiza um numero real entre 0 e 1

print(n1)
print('{:.2f}'.format(n2))

