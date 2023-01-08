from math import floor
distancia = float(input('Qual a distância da sua viagem? '))
if distancia <= 200:  # preco = distancia * 0.50 if distancia <=200 else diatancia * 0.45
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('\033[1;4;7;35;43mO valor do trecho da sua viagem será de R${:.2f}\033[m'.format(floor(preco)))
