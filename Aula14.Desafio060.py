numero = int(input('Digite um número para saber seu fatorial: '))
iterações = numero
fatorial = 1
if numero == 0 or numero == 1:
    fatorial = 1
    print('O resultado de {}! = {}'.format(numero, fatorial))
else:
    print('O valor de {}! ='.format(numero), end=' ')
    while iterações >= 1:
        if iterações > 1:
            print('{} x'.format(iterações), end=' ')
        if iterações == 1:
            print('{} = '.format(iterações), end=' ')
        fatorial = fatorial * iterações
        iterações-= 1
    print(fatorial)
    

"""fat = 1
for i in range(numero, 0, -1):
    fat = i * fat
    i = i - 1
print ('O valor de {}! = {}'.format(numero, fat))"""


