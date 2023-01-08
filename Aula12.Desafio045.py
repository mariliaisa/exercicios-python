from time import sleep
from random import choice
print('VAMOS JOGAR?')
voce = int(input("""Ecolha 
1 - pedra
2 - papel
3 - tesoura:\n"""))
print('Agora é a vez do computador:')
sleep(0.3)
print('JO')
sleep(0.4)
print('KEN')
sleep(0.5)
print('PÔ!!!')
lista = ['pedra','papel', 'tesoura']
jogador = lista[voce - 1]
comp = choice(lista)
sleep(0.7)
print('\033[1;34m''-='*30,'\033[m')
print('O computador escolheu', comp)
if jogador == comp:
    print('Empatou, vamos jogar de novo!')
elif jogador == 'pedra' and comp == 'tesoura' or jogador == 'tesoura' and comp == 'papel' or jogador == 'papel' and comp == 'pedra':
    print('UHUUUUUU Você é o vencedor!!!')
else:
    print('Não foi dessa vez que você superou os Compiuter!!')
print('\033[1;34m''-='*30, '\033[m')