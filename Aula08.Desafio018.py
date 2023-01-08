from math import sin,cos,tan, radians
ang = float(input('Digite o valor do ângulo em graus: '))
print('O seno de {} é {:.2f}'.format(ang, sin(radians(ang))))
print('O cosseno de {} é {:.2f}'.format(ang, cos(radians(ang))))
print('A tangente de {} é {:.2f}'.format(ang, tan(radians(ang))))


