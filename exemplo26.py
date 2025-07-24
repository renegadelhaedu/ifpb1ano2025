nome = 'turma do primeiro ano'  #string
qtde_alunos = 23    #int
nota_media = 87.45 #float
ferias = False  #boolean

#estrutura de decisao simples
if ferias == False and nota_media > 70:
    print('estao todos aprovados e vao curtir a vida')
    ferias = True

#estrutura de decisao composta/encadeada
if qtde_alunos > 1 and qtde_alunos <= 10:
    print('os que estao em sala ganham 20 pontos')
    nota_media += 20
elif qtde_alunos > 10 and qtde_alunos <= 20:
    print('os que estao em sala ganham 10 pontos')
elif qtde_alunos > 20:
    print('os que estao em sala ganham 2 pontos')
else:
    print('irei colocar a prova muito complexa')
    nota_media = nota_media * 0.92
