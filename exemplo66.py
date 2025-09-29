#a aluna ana julia decidiu fazer uma festa de aniversário e não
#pode convidar todo mundo pois o lugar da festa só comporta 10.
#construa um algoritmo que o usuário informe o nome e ele verifique
#se este nome está contido na lista de convidados
convidados = ['ale','adson','pedro','maria','joao','carol','erica','toinho']

nome = input('digite seu nome para saber se voce foi convidado')

if nome in convidados:
    print('voce foi convidado')
else:
    print('infelizmente, nao')