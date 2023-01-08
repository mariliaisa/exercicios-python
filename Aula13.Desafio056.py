mulher = maior = media = 0
homem = ''
for i in range(1,5):
    print('------{}ª PESSOA -------'.format(i))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo[F\M]: ')).strip()
    media += idade
    if sexo in 'mM':
        if idade > maior:
            maior = idade
            homem = nome
    else:
       if idade < 20:
           mulher += 1
print("""
A média de idade é {} anos.
O nome do homem mais velho é {}, com {} anos.
A quantidade de mulheres abaixo de 20 anos é: {}""".format((media/4), homem, maior, mulher))

