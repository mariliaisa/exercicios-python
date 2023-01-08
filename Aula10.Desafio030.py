numero = int(input('Digite um número inteiro: '))
div = numero % 2
if div == 0:
    print('\033[1;30;42mO número {} é par!\033[m'.format(numero))
else:
    print('\033[1;30;45mO número {} é ímpar!\033[m'.format(numero))
