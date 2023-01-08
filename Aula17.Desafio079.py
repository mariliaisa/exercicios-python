import Dicionários as d
d.cabecalho('LISTA CRESCENTE')
valores = []
while True:
    num_inserido = (int(input('Digite um número: ')))
    if num_inserido in valores:
        print('Valor repetido. Tente outro')
    else:
        valores.append(num_inserido)
        print('Valor inserido com sucesso!')
    escolha = d.quer_continuar()
    if escolha == False:
        break
valores.sort()
print(f'\nA lista escolhida foi {valores}')
d.rodape()