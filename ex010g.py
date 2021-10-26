# faça um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento.
# para salarios superiores a 1.250,00 calcule um aumento de 10%.
# para inferiores ou iguais calcule aumento de 15%

salario = float(input('Digite seu salário: R$ '))

if salario > 1250:
    print('Seu salário com aumento de 10% será R$ {:.2f}'.format(salario * 1.1))

else:
    print('Seu salário com aumento de 15% será R$ {:.2f}'.format(salario * 1.15))
