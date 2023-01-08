num = int((input('Digite um número ente 0 e 9999: ')))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
"""milhar = num // 1000
div1 = num % 1000
centena = div1 // 100
div2 = div1 % 100
dezena = div2 // 10
unidade = div2 % 10"""
print('Milhar: {}\nCentena: {}\nDezena: {}\nUnidade: {}'.format(m, c, d, u))
