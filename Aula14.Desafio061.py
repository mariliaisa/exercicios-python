t1 = int(input('Digite o prmeiro termo da sequência que você deseja: '))
r = int(input('Digite a razão da PA: '))
num_termos = int(input('Digite a quantidade de termos da PA: '))
iterações = 0
termo = t1
soma = 0
print('\nOs {} primeiros termos da PA com 1º termo {} e razão {} são:'.format(num_termos, t1, r))
while num_termos > iterações:
    print(termo, end='')
    soma = soma + termo
    termo = termo + r
    iterações += 1
    if iterações != num_termos:
        print(' → ', end='')
print('\nO somatório dos {} termos da PA é: {}'.format(num_termos, soma))
