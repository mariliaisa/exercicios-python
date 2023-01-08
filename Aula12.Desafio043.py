peso = float(input('Digite seu peso: (Kg) '))
altura = float(input('Digite sua altura: (m) '))
imc = peso / (altura**2)
print('Seu IMC é {:.2f}. Esse valor indica que você está'.format(imc),end=' ')
if imc < 18.5:
    print('abaixo do peso, procure um médico!')
elif imc < 25:
    print('no peso ideal, parabéns!')
elif imc < 30:
    print('com sobrepeso, se liga!')
elif imc < 40:
    print('com obesidade, precisa fazer uma dieta!')
else:
    print('com obesidade mórbida, seu caso é muito sério. Procure um médico.')
