r1 = float(input('Digite o comprimento de R1: '))
r2 = float(input('Digite o comprimento de R2: '))
r3 = float(input('Digite o comprimento de R3: '))
if (r1 + r2 > r3) and (r1 + r3 > r2) and (r2 + r3 > r1):
    print("É possível formar um triângulo com as retas dadas!")
else:
    print('Não é possível formar um triângulo com as retas dadas.')



"""if (r1 + r2) > r3:
    if (r1 + r3) > r2:
        if (r2 + r3) > r1:
            print('Pode-se formar um triângulo com as retas de valor {}, {} e {}'.format(r1, r2, r3))
        else:
            print('Não é possível formar um triângulo com as retas dadas.')
    else:
        print('Não é possível formar um triângulo com as retas dadas.')
else:
    print('Não é possível formar um triângulo com as retas dadas.')"""
