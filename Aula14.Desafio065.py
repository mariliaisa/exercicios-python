soma = maior = menor = contador = 0
escolhe = 'S'
while escolhe in 'sS':
    num = int(input('Digite um número: '))
    soma += num
    contador += 1
    if contador == 1:
        maior = menor = num
    maior = max(num, maior)
    menor = min(num, menor)
    escolhe = ''
    while escolhe != 'S' and escolhe != 'N': #ESSE BLOCO É UM TESTE DE ERRO DE DIGITAÇÃO!
        escolhe = str(input('Deseja digitar mais números?[S/N]: ')).upper().strip()[0]
        if escolhe != 'S' and escolhe != 'N':
            print('Opção inválida! Tente novamente.')  
media = soma / contador
print("""
A média dos {} números digitados foi: {:.2f}
O maior número foi: {}
O menor número foi: {}""".format(contador, media, maior, menor))


"""
na linha 9:
else:
    if num > maior:
        maior = num 
    if num < menor:
        menor = num"""