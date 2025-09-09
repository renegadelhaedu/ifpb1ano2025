#os alunos do primeiro ano devem construir um algoritmo na linguagem python
#para ler o nome e a nota da prova de física. o algoritmo deve ir lendo até
# que o aluno digite "fim" no campo nome. ao encerrar o programa informa
# a maior nota.

maior = 0
nome = ''
while nome != 'fim':
    nome = input('digite seu nome ')
    if nome == 'fim':
        break
    nota = float(input('digite sua nota '))
    if nota > maior:
        maior = nota

if maior > 100:
    print('essa pessoa digitou um valor invalido')
else:
    print(maior)