#listas é uma estrutura de dados que podemos armazenar
#itens (string, float,lista,etc) de forma sequencial.
#índice inicia sempre em 0 e vai até o tamanho da lista - 1


alunos = ['eduarda','wendell','isabelle','lucas']

presentes = 0

for aluno in alunos:
    print(aluno, ' veio hoje?')
    resposta = input('diga sim ou nao?')
    if resposta.lower() == 'sim':
        presentes += 1

print('estavam presentes em sala: ', presentes, 'alunos')



