op = 350
while op != 0:
    print('----x---MENU---x----')
    print('1-ler nome do crush do professor Renê')
    print('2-verificar se o crush está disponível')
    print('0-sair')

    op = int(input('digite a opcao desejada '))

    if op == 1:
        crush = input('digite o nome do seu crush')
        if crush == 'Laysla':
            print('uhuuuuu. essa é a pessoa que eu queria')
        else:
            print('essa nao é a pessoa que eu gostaria, desculpe')
