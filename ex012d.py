# Programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade:
# Se ainda vai se alistar, se é a hora de se alistar ou se passou do prazo
# Mostrar tambem o tempo que falta ou que já passou

print('-'*55)
print('\033[7;32mVeja sua situação em relação ao alistamento militar!\033[m')
print('-'*55)

nasc = int(input('Primeiro, digite seu ano de nascimento: '))

from datetime import date
ano = date.today().year     # para pegar o ano atual

if ano - nasc < 18:
    print("\033[1;36mAinda faltam {} ano(s) para você se alistar!\033[m".format(18-(ano-nasc)))

elif ano - nasc == 18:
    print('\033[1;32mEstá na hora de você se alistar!\033[m')

else:
    print('\033[1;31mJá passou {} ano(s) do prazo de alistamento!\033[m'.format((ano-nasc)-18))