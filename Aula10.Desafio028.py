from random import randint as sorte
import time
numero = sorte(0,5)
escolhido = int(input('Escolha um número entre zero e cinco: '))
print('PROCESSANDO...')
time.sleep(0.75)
print('A máquina escolheu {} e tu escolhesse {}'.format(numero, escolhido))
if escolhido == numero:
    print('ACERTOU, MISERÁVI!')
else:
    print('Foi triste, perdesse!')
