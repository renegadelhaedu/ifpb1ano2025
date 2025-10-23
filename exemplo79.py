confra = [['adson','rene']]

op = 99

while op != 0:
    print('\n\n1-Inserir convidado')
    print('2-Editar convidado')
    print('3-Mostrar convidado')
    print('0-Sair')
    op = int(input('qual a opcao desejada? '))

    if op == 1:
        nome = input('qual seu nome? ')
        convidado = input('qual o nome do convidado? ')

        confra.append([nome, convidado])

    elif op == 2:
        nome = input('qual seu nome? ')
        for dupla in confra:
            if nome == dupla[0]:
                dupla[1] = input('quem é o novo convidado? ')
                print(dupla)
                break

    elif op == 3:
        nome = input('qual seu nome? ')
        achei = False
        for dupla in confra:
            if nome == dupla[0]:
                achei = True
                print(f'{dupla[0]} vai levar {dupla[1]}')
                break

        if not achei:
            print('essa pessoa nao foi encontrada')