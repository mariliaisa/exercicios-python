import Dicionários as d
tupla = ('zero', 'um', 'dois','três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    print('*'* 30)
    while True:
        numero = str(input('Digite um número entre 0 e 20: '))
        if numero.isnumeric() and 0 <= int(numero) <= 20: # teste para saber se digitaram certo ou  não
            numero_escolhido = int(numero)
            break
        print('Tente novamente.', end=' ')
    print(f'Você digitou o número {tupla[numero_escolhido]}')
    continuar = d.quer_continuar() # chamei a função que criei para perguntar se qur continuar o programa ou não
    if continuar == False:
        break
print('*'* 30)
print('FIM DO PROGRAMA')


