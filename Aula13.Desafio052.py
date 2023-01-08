from time import sleep
num = int(input('Digite um número: '))
print('Ele é ou não é primo?\nAnalisando...')
sleep(0.75)
div = 0
for i in range(1,num+1):
    if num % i == 0:
        print('\033[1;31m{}\033[m'.format(i), end=' ')
        div += 1
    #else:
        #print('\033[1;m', end='')
    #print('{}'.format(i), end=' ')
if div > 2:
    print('\n\033[mO número {} não é primo! Pois ele possui {} divisores'.format(num, div))
else:
    print('\nO número {} é primo!'.format(num))

