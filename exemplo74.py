lista = [['eduarda', False], ['wendell', True], ['isabelle', False], ['lucas', True]]
lista.sort(reverse=True)
print(lista)
for aluno in lista:
    if aluno[1] == False:
        resp = input(f'voce tem certeza que {aluno[0]} faltou?')
        if resp.lower() == 'nao':
            aluno[1] = True

print(lista)
