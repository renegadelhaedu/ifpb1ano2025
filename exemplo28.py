soma = 0
qtde_alunos = 0
idade = int(input('digite a idade do aluno ou aluna '))

while idade > 0:
    qtde_alunos = qtde_alunos + 1
    soma = soma + idade
    idade = int(input('digite a idade do aluno ou aluna '))

media = soma / qtde_alunos
media = round(media, 1)

print('a media foi ', media)

print('a soma das idade é ', soma)
print('estavam em sala',qtde_alunos,'alunos')