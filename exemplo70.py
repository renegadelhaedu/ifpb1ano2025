usuarios = []
op = 99

while op != 0:
    print('Feira sertão - escolham como quiserem')
    print('1-cadastrar família')
    print('2-ia')
    print('3-a')
    print('4-ver os usuario cadastrados')
    print('0-sair')

    op = int(input('digite a opcao desejada '))

    if op == 1:
        # pedir nome, cpf, senha, confirma_senha
        nome = 'fazer input'
        cpf = 'fazer input'
        senha = 'fazer input'

        usuarios.append([nome, cpf, senha])

    elif op == 4:
        for usuario in usuarios:
            print(usuario[0], end=' - ')
            print(usuario[1])



