from math import hypot
c1 = float(input('Digite o valor do cateto oposto: '))
c2 = float(input('Digite o valor do cateto adjascente: '))
hip = hypot(c1,c2)
print('O valor da hipotenusa do triângulo retângulo com os catetos de valor {} e {} é: {:.2f}'.format(c1,c2,hip))
