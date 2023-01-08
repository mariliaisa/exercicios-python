from time import sleep
num = int(input('Digite o número o que você quer saber a tabuada: '))
print('\nTABUADA DO {}'.format(num))
print('=-'* 6)
print('CALCULANDO...')
sleep(0.75)
for c in range(1, 11):
    tabuada = num * c
    print('\033[1;35m{}\033[m x \033[1;36m{:2}\033[m = \033[1;33m{}\033[m'.format(num, c, tabuada))
print('=-'* 6)
