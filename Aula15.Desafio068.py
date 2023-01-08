from random import randint
vitorias = 0
print('VAMOS JOGAR?')
print('-*' * 20)
while True:
    num_computador = randint(0,10)
    escolha = str(input('Você quer PAR ou ÍMPAR [P/I]? ')).strip().upper()[0]
    num_jogador = int(input('Escolha seu número: '))
    if escolha not in 'pPiI':
        print('Opção inválida!')
    else:
        soma = num_computador + num_jogador
        if soma % 2 == 0:
            resultado = 'PAR'
        else:
            resultado = 'ÍMPAR'
        if escolha == 'P':
            opção_jogador = 'PAR'
            opção_computador = 'ÍMPAR'
        else:
            opção_jogador = 'ÍMPAR'
            opção_computador = 'PAR'
        print(f'\nO computador escolheu {num_computador}')
        if resultado == opção_jogador:
            vitorias += 1
            print(f'UHUUUUUUUU! A soma foi {soma}. DEU {resultado} e você escolheu certinho!')
        else:
            print(f'QUE PENA! A soma foi {soma}. DEU {resultado}, não foi dessa vez!')
            print(f'Depois de {vitorias} vitória(s) você foi derrotado!')
            break
        