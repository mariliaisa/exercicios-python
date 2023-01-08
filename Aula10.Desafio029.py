velocidade = float(input('Digite a velocidade que você estava: '))
if velocidade <= 80:
    print('\033[1;30;42m{}km/h...Segue teu caminho jovem, tua velocidade tá tranquila!\033[m'.format(velocidade))
else:
    print('\033[1;33;41mTais pensando que é o Papa-Léguas é? {}km/h, bicho!\033[m'.format(velocidade))
    excedente = (velocidade - 80) * 7
    print('\033[1;33;41mSó por isso tu vai pagar essa multa de R${:.2f}!\033[m'.format(excedente))
