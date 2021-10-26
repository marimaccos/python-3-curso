# faça um programa que leia uma frase pelo teclado e mostre:
# quantas vezes aparece a letra 'a'
# em que posição ela aparece a primeira vez
# em que posição ela aparece por último

frase = input('Digite uma frase: ').strip().lower()

print('A frase digitada foi:', frase)
print('A letra "a" aparece {} vezes.'.format(frase.count('a')))
print('A primeira letra "a" aparece na posição {}.'.format(frase.find('a')))
print('A última letra "a" aparece na posição {}.'.format(frase.rfind('a')))
