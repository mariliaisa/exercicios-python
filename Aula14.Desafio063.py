"""SEQUÊNCIA DE FIBONACCI:   0 1 1 2 3 5 8 13..."""
quant_termos = int(input('Digite quantos termos da sequência Fibonacci você quer: '))
iteraçoes = 0
anterior1 = anterior2 = atual = 0

while quant_termos > iteraçoes:
    if iteraçoes == 1:               #i = 0 e i = 1 são as duas primeiras iterações, onde não há termos ainda.
        atual = anterior1 = 1        # por isso foi atribuído o valor 1 nas variáveis, sendo o 1º e 2º termos de Fibonacci
    else:                            #i = 2 é exatamente a terceira iteração, que é onde a soma dos termos anteriores começa
        atual = anterior1 + anterior2
        anterior2 = anterior1
        anterior1 = atual
    print(atual, end=' ')
    iteraçoes += 1
    if iteraçoes < quant_termos:
        print(' → ', end='')