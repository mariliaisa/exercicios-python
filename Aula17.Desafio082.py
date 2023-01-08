import Dicionários as d
valores = []
#Formando a lista através de inputs:
while True:
    valores.append(int(input('Digite um número: ')))
    escolha = d.quer_continuar()
    if escolha == False:
        break
#criando novas listas para mostrar só pares ou só impares.
pares = valores.copy()
impares = valores.copy()
#percorrendo a lista principal, comparando os elementos e removendo os impares da lista par;
for numero in valores:
    if numero % 2 == 1:
        pares.remove(numero)
#percorrendo a lista principal, comparando os elementos e removendo os impares da lista par;
for numero in valores:
    if numero % 2 == 0:
        impares.remove(numero)
print(f'A lista gerada foi: {valores}')
print(f'A lista de pares é: {pares}')
print(f'A lista de ímpares é: {impares}')