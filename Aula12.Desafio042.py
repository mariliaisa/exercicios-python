r1 = float(input('Digite o comprimento de R1: '))
r2 = float(input('Digite o comprimento de R2: '))
r3 = float(input('Digite o comprimento de R3: '))
if (r1 + r2 < r3) and (r1 + r3 < r2) and (r2 + r3 < r1):
    print("Não é possível formar um triângulo com as retas dadas!")
else:
    print('É possível formar um triângulo com as retas dadas. Além disso o triângulo formado é', end=' ')
    if r1 == r2 == r3:
        print('equilátero, ou seja, possui todos os lados iguais!')
    elif r1 != r2 != r3 != r1: 
        print('escaleno, ou seja, possui todos os lados diferentes!')
    else:
        print('isósceles, ou seja, possui dois lados iguais e um diferente!')
