#estrutura de repetição for

maior = 0
nome_maior = ''
for cadeira in range(27):
    nome = input('digite seu nome')
    n1 = float(input('digite sua primeira nota'))
    n2 = float(input('digite sua segunda nota'))
    media = (n1 + n2) / 2
    if media > maior:
        nome_maior = nome
        maior = media

if nome_maior == 'rafael':
    print('mesmo sendo a maior nota, nao passara pois thalita determinou')
