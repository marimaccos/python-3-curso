# escreva um programa que faça o computador "pensar" em um numero inteiro entre 0 e 5 e
# peça para o usuario tentar descobrir qual foi o numero escolhido pelo computador. escreva
# se o usuario venceu ou perdeu

import random
from time import sleep

print('Quero ver você advinhar o número que estou pensando! Vou escolher um número entre 0 e 5, tente advinhar!')

nu = int(input('Digite o número que você acha: '))
nv = random.randint(0, 5)

print('Carregando...')
sleep(3)  # espera 3 segundos

if nv == nu:
    print('Isso mesmo! Eu estava pensando no', nv)

else:
    print('Que pena! Eu estava pensando no', nv)
