num = int(input('Quantas pessoas serão comparadas? '))
maior = 0 
menor = 0
for i in range(1, num + 1):
    peso = float(input('Qual o peso da pessoa {}: '.format(i)))
    if i == 1:
        maior = menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso é {}kg e o menor peso é {}kg'.format(maior, menor))




