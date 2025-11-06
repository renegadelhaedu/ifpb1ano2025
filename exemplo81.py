
def verificar_nome():
    nome_completo = input('diga seu nome completo')
    parte_nome = input('diga qual nome quer verificar')
    if parte_nome in nome_completo:
        return True
    else:
        return False


if verificar_nome():
    print('esse nome ta dentro do completo')
else:
    print('nao está contido')

