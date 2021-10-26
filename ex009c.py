# crie um programa que leia o nome de uma cidade e diga se ela começa ou nao com o nome "Santo"

nome = input('Digite o nome de uma cidade: ').strip()  #tirar os espaços do inicio e fim da palavra
t = nome.title()
div = t.split()
primeiro = div[0]

print('A cidade foi:', t)
print('Essa cidade começa com o nome Santo?', 'Santo' in primeiro)
print('Essa cidade começa com o nome Santo?', nome[:5].title() == 'Santo')  # seleciona as primeiras 4 letras do nome
