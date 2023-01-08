from time import sleep
escolher = 0
while escolher !=5:
    if escolher == 0 or escolher == 4:
        valor1 = float(input('Digite o primeiro valor: '))
        valor2 = float(input('Digite o segundo valor: '))
    sleep(0.5)
    print('-*' * 20)
    escolher = int(input("""
Escolha entre as seguintes opções:
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA
"""))
    sleep(0.5)
    print('-*' * 20)
    if escolher == 1:
        soma = valor1 + valor2
        print('A soma dos valores escolhidos é: {}'.format(soma))
    elif escolher == 2:
        produto = valor1 * valor2
        print('O produto dos valores escolhidos é: {}'.format(produto))
    elif escolher == 3:
        maior = valor1
        if valor1 < valor2:
            maior = valor2
            print('O maior número é: {}'.format(maior))
        if valor1 == valor2:
            print('Os números são iguais!')
    elif escolher == 5:
        print('FIM!')
    if escolher !=1 and escolher !=2 and escolher !=3 and escolher !=4 and escolher !=5:
        print('Opção inválida! Digite outra opção.') 
