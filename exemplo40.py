#questao 3 feita em sala no dia 14 de agosto

nome =  'm'
qtde_sem = 0
while nome != 'fim':
    if 'm' in nome:
        print(' ')
    else:
        qtde_sem += 1
    nome = input('digite seu nome')


print('a quantidade de pessoas sem M foi', qtde_sem)