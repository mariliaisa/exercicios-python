larg = float(input('Qual a largura da parede? '))
alt = float(input('Qual a altura da parede? '))
a = larg * alt
print('A Área da parede é de {}m²\nPara pintar a parede, serão necessários {:.2f}l de tinta'.format(a, a/2))
