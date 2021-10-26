# exemplos de usos dentro da máscara de formatação

nome = input('Qual é o seu nome? ')

print('Prazer em te conhecer, {}!'.format(nome))
print('Prazer em te conhecer, {:10}!'.format(nome))
print('Prazer em te conhecer, {:<10}!'.format(nome))
print('Prazer em te conhecer, {:>10}!'.format(nome))
print('Prazer em te conhecer, {:^10}!'.format(nome))
print('Prazer em te conhecer, {:=^10}!'.format(nome))

