valores = []
for c in range(0,5):
    numero = int(input('Digite um número: '))
    if c == 0 or numero > valores[-1]:
        valores.append(numero)
        print('Adicionado ao final da lista.')
    else:
#percorrendo a lista por índice!
        posicao = 0
        while posicao < len(valores):
            if numero <= valores[posicao]: # numero digitado comparado ao elemento da lista referente a posição.
                valores.insert(posicao, numero)
                print(f'Adicionado na posição {posicao + 1} da lista.')
                break
            posicao +=1
print(f'Os valores da lista foram: {valores}')

