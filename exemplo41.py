somaletras = 0
qtde_pessoas = 0
while somaletras <= 10:
    nome = input('digite seu nome')
    somaletras = somaletras + len(nome)
    qtde_pessoas += 1

media = somaletras / qtde_pessoas

print('a quantidade de pessoas lidas foi', qtde_pessoas)
print('em media, essas pessoas tinham essa qtde de letras no nome', media)