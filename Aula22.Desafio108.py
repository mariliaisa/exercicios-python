from utilidadesCEV import moeda
num = float(input('Digite um preço: R$ '))

print(f'O dobro de {moeda.moeda(num)} é: ')
print(moeda.moeda(moeda.dobro(num)))
print(f'A metade de {moeda.moeda(num)} é: ')
print(moeda.moeda(moeda.metade(num)))
print(f'Aumento de 10% em {moeda.moeda(num)} é: ')
print(moeda.moeda(moeda.aumenta(num, 10)))
print(f'Decréscimo de 10% em {moeda.moeda(num)} é: ')
print(moeda.moeda(moeda.diminui(num, 10)))