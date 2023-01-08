#FUNÇÃO PARA MOSTRAR O MAIOR VALOR
from time import sleep
def maior(*num):
    print('-='*20)
    print('Analisando os valores passados...')
    if len(num) == 0:
        print('Não foi informada nenhuma sequência.')
    else:
        for i in num:
            print(i, end=' ', flush=True)
            sleep(0.5)  
        print()
        print('-='*20)
        sleep(0.7)
        print(f'Foram informados {len(num)} valores ao todo e o maior foi {max(num)}')


maior(1,5,6,9,8,3,6,7)
maior(2,8,75)
maior(1,63)
maior(5)
maior()

