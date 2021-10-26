# Programa para aprovar o empréstimo bancário para a compra de uma casa.
# Perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado

print('\033[34;43mOlá! Para verificar se seu empréstimo será aprovado digite as seguintes informações:\033[m')

valor = float(input('Digite o valor do imóvel: R$'))
salário = float(input('Digite seu salário: R$'))
anos = int(input('Digite em quantos anos você pretente pagar: '))

prestação = valor / anos

if prestação <= (0.3 * salário):
    print('\033[32mParabéns! Seu empréstimo será aprovado!\033[m')

else:
    print('\033[31mInfelizmente seu empréstimo foi negado!\033[m')
