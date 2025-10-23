#listas é uma estrutura de dados que podemos armazenar
#itens (string, float,lista,etc) de forma sequencial.
#índice inicia sempre em 0 e vai até o tamanho da lista - 1


alunos = ['eduarda','wendell','isabelle','lucas']
presenca = []

for alunao in alunos:
    resposta = input(f'oa estudante {alunao} esta em sala?')
    if resposta.lower() == 'sim':
        presenca.append([alunao, True])
    else:
        presenca.append([alunao, False])

print(presenca)
