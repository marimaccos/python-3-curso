# Programa que leia o ano de nascimento de um atleta a mostra sua categoria, de acordo com a idade

print(35*'-')
print('\033[1;34mCONFEDERAÇÃO NACIONAL DE NATAÇÃO\033[m')
print(35*'-')

from datetime import datetime   # Módulo para pegar data atual

now = datetime.now()    # Pega a data completa
ano = int(input('Digite seu ano de nascimento para saber sua categoria: '))

if (now.year-ano)<=9:   # Pegar só o ano da data
    print('MIRIM')

elif 9 < (now.year-ano) <= 14:
    print('INFANTIL')

elif 14 < (now.year-ano) <= 19:
    print('JUNIOR')

elif 19 < (now.year-ano) <= 20:
    print('SÊNIOR')

else:
    print('MASTER')

