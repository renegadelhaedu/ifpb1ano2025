alunos = ''
novo = input('qual o nome do aluno').lower()
while novo != 'nao':
    if 'caetano' in novo:
        print('deixe de invençao que eu sei que ele nao veio hoje')
    else:
        alunos = alunos + ' , ' + novo
    novo = input('qual o nome do aluno').lower()

print(alunos)
