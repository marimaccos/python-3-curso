# faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos
# separados unidade/dezena/centena/milhar

num = int(input('Digite um número de 0 a 9999: '))

print('Seu número foi', num)
print('Unidades:', (num//1) % 10)  # número e sua divisão inteira por 1 depois módulo de 10 (divide por 10 e pega o resto)
print('Dezenas:', (num//10) % 10)  # número pela divisão inteira por 10 depois módulo de 10
print('Centenas:', (num//100) % 10)  # número pela divisão inteira por 100 depois módulo de 10
print('Milhares:', (num//1000) % 10)  # número pela divisão inteira por 1000 depois módulo de 10
