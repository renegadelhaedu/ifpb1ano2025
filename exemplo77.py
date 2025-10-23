alunos = ['ana julia','eduarda','wendell','isabelle','lucas']

nome = input('quem vc quer remover?')
if nome in alunos:
    alunos.remove(nome)
else:
    print('essa pessoa nao está na lista')

print(alunos)