import time
num = int(input('Digite um número inteiro: '))
print('Para qual base você quer convertê-lo?')
escolhe = int(input('\033[1;32m1 - Binária;\033[m\n\033[1;35m2 - Octal;\033[m\n\033[1;34m3 - Hexadecimal:\033[m\n'))
print('\033[1;32mProcessando...\033[m')
time.sleep(0.75)
if escolhe == 1:
    print('\033[1;32mO número {} convertido para base binária é: {}\033[m'.format(num, bin(num)[2:]))
elif escolhe == 2:
    print('\033[1;35mO número {} convertido para a base Octal é: {}\033[m'.format(num, oct(num)[2:]))
elif escolhe == 3:
    print('\033[1;34mO número {} convertido para base hexadecimal é: {}\033[m'.format(num, hex(num)[2:]))
else:
    print('Opção INVÁLIDA. Escolha umas das opções válidas.')

"""As funções bin(), oct() e hex() retornam uma string, então é possível fazer o fatiamento dessa string
para que não apareçam os prefixos das conversões"""