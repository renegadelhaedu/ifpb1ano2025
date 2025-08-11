#o ifpb decidiu chamar os alunos para almoçarem em sao gonçalo.
#a aluna Yhorranyh revoltada com o tamanho da fila, resolveu
#desenvolver um algoritmo em python para impedir que seres "humanos"
#furem a fila. ela tem uma desculpa que a gente nao acredita

pedido = ''
qtde_alunos = 0
while pedido != 'nada':
    pedido = input('o que voce quer comer?')
    if 'prea' in pedido:
        print('nos nao trabalhamos com isso')
    else:
        print('seu prato vai ser servido agora')
    qtde_alunos += 1

print('a quantidade de alunos que comeram foi', qtde_alunos)
