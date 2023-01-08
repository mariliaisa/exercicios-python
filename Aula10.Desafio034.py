salario = float(input('Informe o valor do seu salário: R$'))
if salario <= 1250:
    aumento = salario * 1.15
else:
    aumento = salario * 1.10
print('O seu novo salário, com o aumento será de: R${:.2f}'.format(aumento))
