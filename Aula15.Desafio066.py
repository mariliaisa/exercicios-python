contador = soma = 0
while True:
    num = int(input('Digite um número inteiro [999 para parar]: '))
    if num == 999:
        break       
    soma += num
    contador += 1
print(f'o somatório dos {contador} números digitados é: {soma}')