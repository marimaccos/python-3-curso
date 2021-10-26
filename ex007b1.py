# método com menos variáveis
n = int(input('Digite um número: '))

print('O dobro de {} é {}, o triplo de {} é igual a {}'.format(n, (n*2), n, (n*3)))
print('A raiz de {} vale {:.2f}'.format(n, (n**(1/2))))

# outro método de raiz é pela função pow
print('A raiz de {} é {:.2f}'.format(n, pow(n, (1/2))))

