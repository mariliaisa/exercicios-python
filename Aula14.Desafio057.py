sexo = ''
while (sexo != 'F' and sexo !='M'):
    print('Dados inválidos! Digite seu sexo: ')
    sexo = str(input('Digite o seu sexo: ')).upper().strip()
if sexo in 'fF':
    print('Seu sexo é feminino!')
elif sexo in 'mM':
    print('Seu sexo é masculino!')
    

"""OUTRA FORMA:
while sexo not in 'fFmM:
    print('Dados inválidos! Digite seu sexo: ')
print('Sexo {} registrado com scesso.'.format(sexo)).upper().strip()
"""

