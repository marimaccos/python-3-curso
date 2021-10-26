# programa para calcular a média de duas notas de um aluno e mostre a situação final

print('\033[1;31mCálculo de média\033[m')

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
média = (n1+n2)/2

if média < 5:
    print('\033[7;31mREPROVADO\033[m')

elif 5 <= média < 6.9:
    print('\033[7;33mRECUPERAÇÃO\033[m')

else:
    print('\033[7;32mAPROVADO\033[m')
