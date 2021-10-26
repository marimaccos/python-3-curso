# Condições simples, compostas e simplificadas

nome = str(input('Digite o nome do aluno: '))
n1 = float(input('Digite a priemira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
media = (n1+n2+n3)/3

print('A média foi: {:.1f}'.format(media))

if media >= 7.0:
    print('{} foi aprovado!'.format(nome))

else:
    print('{} foi reprovado!'.format(nome))

# print('Parabens!' if media>=7 else 'Estude mais!')  # condição simplificada
