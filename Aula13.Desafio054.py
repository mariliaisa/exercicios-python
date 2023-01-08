from time import time
from datetime import date
atual = date.today().year
maior = 0
menor = 0
quant = int(input('Qual a quantidade de pessoas a serem avaliadas? '))
for i in range(1,quant + 1):
    ano_nasc = int(input('Qual o ano do seu nascimento? '))
    idade = atual - ano_nasc
    if idade < 21:
        menor += 1
    else:
        maior += 1
print('Há {} pessoas menores de idade\nHá {} pessoas maiores de idade'.format(menor, maior))
