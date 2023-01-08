from utilidadesCEV import moeda
num = float(input('Digite um preço: R$ '))

print(f'O dobro de {moeda.moeda(num)} é: ')
print(moeda.dobro(num, mostrar = True))
print(f'A metade de {moeda.moeda(num)} é: ')
print(moeda.metade(num, mostrar =True))
print(f'Aumento de 10% em {moeda.moeda(num)} é: ')
print(moeda.aumenta(num, mostrar = True))
print(f'Decréscimo de 10% em {moeda.moeda(num)} é: ')
print(moeda.diminui(num, mostrar = True))