#laços de repetição (for e while)
#break: interrompe a repetição e sai do laço
#continue: volta para o início do laço


qtde = 0

while True:
    op = int(input('1-aluno\n0-sair  '))

    if op == 1:
        qtde += 1
        continue
    elif op == 0:
        break

    print('opçao inválida')

print('a quantidade de alunos é ', qtde)
