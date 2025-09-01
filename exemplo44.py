op = -1

while op != 0:
    print('1-ler o nome')
    print('2-saber se o nome é composto')
    op = input('digite sua opcao')
    if op == '1':
        nome = input('digite seu nome')
    elif op == '2':
        if ' ' in nome:
            print('seu nome é composto')
        else:
            print('seu nome nao é composto')
    else:
        break

print('acabou, chegou ao fim, igual a simone e simara')