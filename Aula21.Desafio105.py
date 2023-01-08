def notas(*n, sit=False):
    notasAluno = dict()
    notasAluno['quantidade'] = len(n)
    notasAluno['maior'] = max(n)
    notasAluno['menor'] = min(n)
    notasAluno['média']= sum(n)/len(n)
    if sit:
        if notasAluno['média'] < 5:
            status = 'SITUAÇÃO DE MORTE'
        elif 5 <= notasAluno['média'] <= 7:
            status = 'Ainda dá pra se salvar'
        else:
            status = 'Coisa linda de se ver!'
        notasAluno['sit'] = status
    return notasAluno


resultado = notas(5, 6, 10, sit=True)
print(resultado)
print('-='* 20)
resultado = notas(10, 8, 10, sit=True)
print(resultado)
print('-='* 20)     
resultado = notas(5, 6, 2, sit=True)
print(resultado)
print('-='* 20)