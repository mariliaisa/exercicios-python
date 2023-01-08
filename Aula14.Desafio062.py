t1 = int(input('Digite o prmeiro termo da sequência que você deseja: '))
r = int(input('Digite a razão da PA: '))
escolha = True
termo = t1
i = soma = total = 0

while escolha:
    num_termo = int(input('\nDigite a quantidade de termos da PA que você quer: '))
    i = 0
    print('Os {} primeiros termos da PA com 1º termo {} e razão {} são:'.format(num_termo, t1, r))
    while num_termo > i:
        print(termo, end='')
        soma = soma + termo
        termo = termo + r
        i += 1
        total += 1
        if i != num_termo:
            print(' → ', end='')
    if num_termo == 0:
        escolha = False
print('\nO somatório dos {} termos da PA é: {}'.format(total, soma))