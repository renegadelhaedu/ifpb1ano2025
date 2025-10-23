italo_rafael = []

for i in range(6):
    nome = input('qual teu nome ')
    prato = input('qual seu prato preferido ')

    italo_rafael.append([nome, prato])

qtde = 0
for aluno in italo_rafael:
    if aluno[1] == 'feijoada':
        qtde = qtde + 1
        print(f'{aluno[0]} ama feijoada')

print(f'\n{qtde} pessoas amam feijoada')