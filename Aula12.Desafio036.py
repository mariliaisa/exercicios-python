valor_casa = float(input('Qual o valor da casa que você deseja comprar? R$'))
salario = float(input('Qual o seu salário? R$'))
anos = int(input('Em quantos anos você vai pagar o valor da casa? '))
prestação = valor_casa / (anos * 12)
valor_maximo = 0.3 * salario
if prestação <= valor_maximo:
    print('\033[1;34mO seu empréstimo foi aprovado!')
    print('O valor das parcelas pela nossa simulação é de R${:.2f}'.format(prestação))
else:
    print('\033[1;31mInfelizmente o seu empréstimo foi negado.')
