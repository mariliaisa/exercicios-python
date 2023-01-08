contador = soma = 0
escolha = True
while escolha:
    num = int(input('Digite um número inteiro [999 para parar]: '))
    if num != 999:
        soma += num
        contador += 1
    else:
        escolha = False
print('o somatório dos {} números digitados é: {}'.format(contador, soma))