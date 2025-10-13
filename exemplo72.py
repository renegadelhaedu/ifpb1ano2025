paqueras = [['ana maria', 22], ['cleide', 20], ['erica', 111]]

op = 88
while op != 0:
    print('\n\n-----MENU----')
    print('1-cadastrar paquera')
    print('2-listar paqueras')
    print('3-remover paquera')
    print('0-sair')

    op = int(input('digite a opcao desejada'))

    if op == 1:
        nome = input('qual seu nome no instagram?')
        idade = int(input('qual sua idade?'))
        paqueras.append([nome, idade])
    elif op == 2:
        print('\nLista de paqueras:')
        if len(paqueras) > 0:
            for p in paqueras:
                print('nome:', p[0],' - idade:',p[1])
        else:
            print('essa pessoa nao tem paqueras')

    elif op == 3:
        for i in range(len(paqueras)):
            print(i,' - nome: ', paqueras[i][0])

        indice = int(input('informe o indice da pessoa para remover'))
        paqueras.pop(indice)
