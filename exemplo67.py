#a aluna ana julia decidiu fazer uma festa de aniversário e não
#pode convidar todo mundo pois o lugar da festa só comporta 10.
#construa um algoritmo que o usuário informe o nome e ele verifique
#se este nome está contido na lista de convidados
convidados = ['ale','adson','pedro','maria','joao','carol','erica','toinho']
confirmados = 0
for nome in convidados:
    resposta = input(nome + ', voce vai ou nao para a festa?')
    if resposta == 'sim':
        confirmados += 1

print('ana julia, a quantide confirmada foi ', confirmados)