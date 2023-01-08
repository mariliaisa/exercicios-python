print('{}{:=^40}{}'.format('\033[1;35m', 'LOJA DA MARÍLIA', '\033[m'))
produto = float(input('\nDigite o valor do produto: R$'))
print('Qual a condição de pagamento?')
pgto = int(input("""
1) À vista (dinheiro/cheque) - 10% de desconto
2) À vista (cartão) - 5% de desconto
3) 2x no cartão - preço normal
4) 3x ou mais no cartão - 20% de juros\n"""))
if pgto != 1 and pgto != 2 and pgto != 3 and pgto != 4:
    print('OPÇÃO DE PAGAMENTO INVÁLIDA!')
else:
    if pgto == 1:
        nproduto = 0.9 * produto
    elif pgto == 2:
        nproduto = 0.95 * produto
    elif pgto == 3:
        nproduto = produto
    elif pgto == 4:
        num_parcelas = int(input('Em quantas parcelas você deseja pagar? '))
        nproduto = 1.20 * produto
        nparcelas = nproduto / num_parcelas
        print('\nO valor da sua compra será dividido em {} parcelas de R${}'.format(num_parcelas, nparcelas))
    print('O valor a ser pago de acordo com a condição escolhida é R${}'.format(nproduto))


