import Dicionários as d
valores = []
#Montando a lista através de inputs
while True:
    valores.append(int(input('Digite um número: ')))
    escolha = d.quer_continuar()
    if escolha == False:
        break
#Mostrando os resultados de acordo como pedido:
print(f'\nA lista digitada foi: {valores}')
#Quantidade de elementos da lista:
print(f'Foram digitados {len(valores)} números na lista.')
#Colocando a lista em ordem decrescente:
valores.sort(reverse=True)
print(f'A lista em ordem descrescente é: {valores}')
#Percorrendo a lista e imprimindo a posição do número 5, se ele existir na lista.
print(f'Há {valores.count(5)} número(s) 5 na lista na(s) posição(s): ')
for i, numero in enumerate(valores):
    if numero == 5:
        print(i, end=' ')
    
    