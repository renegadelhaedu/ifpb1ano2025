qtde_pessoas = 1
tops = 0
while qtde_pessoas <= 7:
    print('dança número ', qtde_pessoas)
    nota = int(input('qual sua nota para essa dança?'))
    if nota >= 9:
        tops += 1

    qtde_pessoas += 1

print('Rafael encontrou ', tops, ' profissionais da danca')