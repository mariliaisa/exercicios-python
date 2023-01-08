from random import randint as sorte
from time import sleep

numero_computador = sorte(0,10)
acertou = True
#print(numero)
tentativas = 0
print('VAMOS BRINCAR? Pensei em um número entre 0 e 10, será que você consegue adivinhar?')
while acertou:
    numero_jogador= int(input('Dê o seu palpite: '))
    tentativas += 1  
    if numero_jogador == numero_computador:
        acertou = False
        print('\nACERTOU, MISERÁVI!')
    if numero_jogador < numero_computador:
        print('MAIS... tente outro número: ')
    elif numero_jogador > numero_computador:
        print('MENOS... tente outro número:' )
sleep(0.75)
print('A máquina escolheu {} e tu escolhesse {}'.format(numero_computador, numero_jogador))
print('Depois de {} tentativas!'.format(tentativas))
