print('{:*^50}'.format('CAIXA ELETRÔNICO'))
nota_50 = nota_20 = nota_10 = nota_1 = 0
escolha = True
while True:
    while escolha == True:
        print('='* 50)
        valor_solicitado = str(input('Quanto você quer sacar? R$')).strip().upper()
        if valor_solicitado.isnumeric():
            valor_saque = int(valor_solicitado)
            escolha = False
    if valor_saque >= 50:
        valor_saque -= 50
        nota_50 += 1
    elif valor_saque >= 20:
        valor_saque -= 20
        nota_20 += 1
    elif valor_saque >= 10:
        valor_saque -= 10
        nota_10 += 1
    elif valor_saque >= 1:
        valor_saque -= 1
        nota_1 += 1
    else:
        break
print(f'VOCÊ SACOU R${int(valor_solicitado)} E RECEBERÁ:')
if nota_50 !=0:
    print(f'{nota_50} nota(s) de R$50,00')
if nota_20 !=0:
    print(f'{nota_20} nota(s) de R$20,00')
if nota_10 !=0:
    print(f'{nota_10} nota(s) de R$10,00')
if nota_1 !=0:
    print(f'{nota_1} nota(s) de R$1,00')
print('=' * 50)


"""OUTRA FORMA: SEM O while:
nota_50 = valor_saque // 50
sobra1 = valor_saque % 50
nota_20 = sobra1 // 20
sobra2 = sobra1 % 20
nota_10 = sobra2 // 10
sobra3 = sobra2 % 10
nota_1 = sobra3 // 1"""

            