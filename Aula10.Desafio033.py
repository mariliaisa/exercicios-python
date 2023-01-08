a = float(input('Digite o primeiro número: '))
b = float(input('Digite o segundo número: '))
c = float(input('Digite o terceiro número: '))
menor = a
if b < a and c < a:
    menor = b
if c < a and c < b:
    menor = c
# verificando quem é maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('\033[1;35mO maior número é\033[m', maior)
print('O menor número é', menor)

"""n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))
lista = [n1, n2, n3]
lista.sort()
print('o menor numero é {} e o maior é {}'.format(lista[0], lista[-1]))"""