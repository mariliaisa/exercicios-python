km = float(input('Quantos km você rodou? '))
dias = int(input('Por quantos dias você alugou o carro? '))
custototal = (km * 0.15) + (dias * 60)
print('O preço pelo aluguel do carro será de: R${:.2f}'.format(custototal))



