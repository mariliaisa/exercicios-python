Alunos = dict()
Alunos['nome'] = str(input('Nome do aluno: ')).strip().capitalize()
Alunos['media'] = float(input('Média do aluno: '))
if Alunos['media'] >= 7:
    Alunos['situação'] = 'Aprovado(a)'
elif 5 <= Alunos['media'] < 7 :
  Alunos['situação'] = 'Recuperação'
else: 
  Alunos['situação'] = 'Reprovado'
print(f'O aluno(a) {Alunos["nome"]}, teve média {Alunos["media"]} e sua situação é {Alunos["situação"]}')
