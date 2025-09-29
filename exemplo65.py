alunos = []

nome = input('digite seu nome para registrar sua presença na aula ou sair para encerrar ')

while nome != 'sair':
    alunos.append(nome)

    nome = input('digite seu nome para registrar sua presença na aula ou sair para encerrar  ')

print('a lista abaixo armazena todos os alunos do 1 ano')
print(alunos)