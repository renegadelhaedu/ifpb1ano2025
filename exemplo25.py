'''
crie um algoritmo para fazer 5 perguntas para desencarlharmos seu(sua) amiga(o). O sistema deve ler o nome do candidato(a) e fazer perguntas em formato de entrevista que as respostas serão do tipo sim, não ou talvez.
O programa deve contar quantos sim, não ou talvez. Isso ajudará o usuário a verificar sua alma gêmea.
'''
qtdenao = 0
qtdesim = 0
qtdetalvez = 0

musica = input('voce gosta de MPB?')
if musica == 'sim':
    qtdesim = qtdesim + 1
elif musica == 'nao':
    qtdenao = qtdenao + 1
else:
    qtdetalvez = qtdetalvez + 1

esporte = input('voce gosta de praticar esporte?')
if esporte == 'sim':
    qtdesim = qtdesim + 1
elif esporte == 'nao':
    qtdenao = qtdenao + 1
else:
    qtdetalvez = qtdetalvez + 1


danca = input('voce gosta de dançar forro?')
if danca == 'sim':
    qtdesim = qtdesim + 1
elif danca == 'nao':
    qtdenao = qtdenao + 1
else:
    qtdetalvez = qtdetalvez + 1

if qtdesim >= 2:
    print('eu acho que a gente vai dar certo pois temos gostos semelhantes')
else:
    print('sinto muito, mas sua alma gemea pode ser outra pessoa')