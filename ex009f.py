# faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o
# priemiro e o ultimo nome separadamente

nome = str(input('Digite seu nome completo: ')).strip().title()
lista = nome.split()

print('Primeiro nome:', lista[0])
print('Último nome:', lista[-1])
print(lista[len(lista)-1])  # número total da lista menos 1
