def verificar_senha(senha, confirmacao):
    if senha != confirmacao:
        return True
    else:
        if len(senha) >= 8:
            return False
        else:
            return True

lista = []

nome = input('dasdasd')
cpf = input('cpgasdas ')
senha = input('')
confirm = input('')

while verificar_senha(senha, confirm):
    print('digite novamente porem com senhas iguais e pelo menos 8 cracatearafsf')
    senha = input('')
    confirm = input('')

lista.append([nome, cpf, senha])
