from utilidadesCEV import moeda
num = float(input('Digite um preço: R$ '))

print(f'O dobro de {num} é: ')
print(moeda.dobro(num))
print(f'A metade de {num} é: ')
print(moeda.metade(num))
print(f'Aumento de 10% em {num} é: ')
print(moeda.aumenta(num, 10))
print(f'Decréscimo de 10% em {num} é: ')
print(moeda.diminui(num, 10))