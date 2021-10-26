# exemplos de utilização de operações aritméticas

n1 = int(input('Digite um valor: '))
n2 = int(input('Outro valor: '))
a = n1+n2
s = n1-n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2

# (end='') juntar linhas do print
# (\n) nova linha, separar linhas do print
print('A soma é {}, a subtração é {},\na multiplicação é {},'.format(a, s, m), end=' ')

# (:.3f) indicar resultado em 3 casas decimais
print('a divisão é {:.3f},\na divisão inteira é {}, e a potência é {}.'.format(d, di, e))
