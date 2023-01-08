frase = str(input('Digite um expressão qualquer que use parênteses: ')).strip()
pilha = []
#comparando se o número de parênteses é igual:
for elemento in frase:
    if elemento == '(':
        pilha.append('(') #adiciona um elemento na pilha
    elif elemento == ')':
        pilha.pop() #deleta o elemento que foi adiconado antes da lista
        
#Verificando o tamanho da lista 'pilha', se os parênteses tem a mesma quantidade, o len(pilha) == 0
if len(pilha) == 0:
    print('Sua expressão está correta!')
else:
    print('Sua expressão não está correta, verifique o número de parênteses.')