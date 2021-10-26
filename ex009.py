# Manipulando texto
frase = "Curso em Video Python"

# Fatiamento
print('-'*20)
print('FATIAMENTO')
print('-'*20)
print(frase[9])
print(frase[9:13])  # do 9 até o 12
print(frase[9:16:2])  # pula de 2 em 2
print(frase[:16])  # começa do início da string
print(frase[9:])  # termina no final da string
print(frase[::3])
print('-'*20)

# Análise
print('ANÁLISE')
print('-'*20)
print(len(frase))  # mostra o número de caracteres da string com espaços
print(frase.count('o'))  # quantas vezes aparece o caractere
print(frase.count('o', 0, 14))  # contagem com fatiamento
print(frase.find('so'))  # quando começa a posição
print(frase.find('Android'))  # quando não existe o resultado é -1
print('Curso' in frase)  # se existe determinado caractere na string
print(frase.upper().count('O'))  # combinação
print('-'*20)

# Transformação
print('TRANSFORMAÇÃO')
print('-'*20)
print(frase.replace('Python', 'Android'))  # "substitur"
print(frase.upper())  # tudo maiúsculo
print(frase.lower())  #tudo minúsculo
print(frase.capitalize())  # só o primeiro caractere em maiúsculo
print(frase.title())  # a primeira de cada palavra maiúscula

frase2 = '   Aprenda Python  '
print(frase2.strip())  # retira espaços do começo e do fim
print(frase2.rstrip())  # retira espaços da direita/fim
print(frase2.lstrip())  #retira espaços da esquerda/começo
print('-'*20)

# Divisão
print('DIVISÃO')
print('-'*20)
print(frase.split())  # divide o string pelos espaços gerando lista com as palavras formadas

dividido = frase.split()
print(dividido[1])  # mostrar a palavra dividida escolhida
print(dividido[2][1])  # mostrar o dividido 2 e mostrar o seu 2o caractere
print('-'*20)

# Junção
print('JUNÇÃO')
print('-'*20)
print('-'.join(frase))

print('-'*20)

# texto em um print
print("""ajshdjadjaj sjdueuefdsj  r3uudajshda fuweuahsuda udfqud
sadhuqwedhassjd ad7u3dajshda fruiohfdquhdq qaudgausghda
erjjenfwiuhdfc ewfjsfsahçfajf ffbsjfbsdjfbsjfb""")
