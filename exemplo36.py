#construa um algoritmo em python que leia o nome de todos os seus colegas e conte quantos alunos tem a letra "a" e "e" no nome

nome = ''
quantidade = 0
while nome != 'acabou':
    nome = input('diz teu nome, doido ou doida').lower()
    if 'a' in nome and 'e' in nome:
        quantidade += 1


print('a quantidade final foi', quantidade)