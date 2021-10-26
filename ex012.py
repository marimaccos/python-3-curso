# Estruturas condicionais aninhadas

nome = str(input('Qual seu nome? '))

if nome == 'Mariana':
    print('Que nome bonito!')

elif nome in "Ana Maria Pedro Lucas Paulo João":
    print('VocÊ tem um nome bem comum!')

elif nome == 'Saori' or nome == 'Gertrudes' or nome == 'Carlota':
    print('Que nome diferente você tem!')

else:
    print('Nome legal!')

print('Tenha um bom dia, {}!'.format(nome))
