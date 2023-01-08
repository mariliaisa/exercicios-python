print('{:*^50}'.format('LOJA MARÍLIA'))
total_de_produtos = mais_caro = mais_barato = 0
nome_barato = ''
while True:
    while True:
        nome_produto = str(input('NOME DO PRODUTO: ')).strip().upper()
        if nome_produto != '':
            break
    while True:
        preco_entrada = str(input('PREÇO DO PRODUTO: R$')).strip()
        if preco_entrada.isnumeric():
            preco_produto = float(preco_entrada)
            break
    while True:
        mais_produtos = str(input('CADASTRAR MAIS PRODUTOS [S/N]? ')).strip().upper()[0]
        if mais_produtos in 'SN':
            break
    if total_de_produtos == 0 or preco_produto < mais_barato:
        mais_barato = preco_produto
        nome_barato = nome_produto
    total_de_produtos += preco_produto
    if preco_produto > 1000:
        mais_caro += 1
    
    if mais_produtos in 'N':
        break
print('{:*^50}'.format('PRODUTOS CADASTRADOS:'))
print("""
TOTAL DA COMPRA: R${:.2f}
PRODUTOS QUE CUSTAM MAIS QUE R$1000,00: {}
PRODUTO MAIS BARATO: {}, que custa R${:.2f}""".format(total_de_produtos, mais_caro, nome_barato, mais_barato))    
