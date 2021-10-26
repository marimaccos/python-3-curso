# crie um programa que leia o nome completo da pessoa e mostre:
# nome com todas letras maiúsculas
# nome com todas letras minúsculas
# quantas letras ao todo sem espaços
# quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo: ')).strip()  # tirar os espaços do início e do fim
dividido = nome.split()

print(nome.upper())
print(nome.lower())
print('Seu nome tem {} letras'.format(len(nome.replace(' ', ''))))  # tirando os espaços entre as palavras
print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))  # tirando os espaços entre as palavras
print('O primeiro nome é {} e tem {} letras'.format(dividido[0], len(dividido[0])))  # contando os caracteres da primeira palavra



