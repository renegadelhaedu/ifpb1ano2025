#faça um programa para o usuário tentar acertar o login e a senha
#3x. No entanto, o login deve possuir '@' e a senha deve ter pelo
#menos 8 caracteres.
logou = False
for i in range(3):
    login = input('digite seu login')
    while '@' not in login:
        login = input('digite seu login novamente')

    senha = input('digite sua senha')
    while len(senha) < 8:
        senha = input('digite sua senha novamente')

    if login == '1ano@ifpb' and senha == 'saonota10':
        logou = True
        break

