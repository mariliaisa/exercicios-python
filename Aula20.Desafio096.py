#Criando uma função para calcular a área de um retângulo
def area(x, y):
    a = x * y
    print(f'A área do seu terreno com dimensões {x:.2f}m x {y:.2f}m é {a:.2f}m²')

#PROGRAMA PRINCIPAL
print('-'* 40)
print('{:^30}'.format('Controle de terreno'))
print('-'* 40)
largura = float(input('Largura (m): '))
altura = float(input('Altura (m): '))
print()
area(largura, altura)