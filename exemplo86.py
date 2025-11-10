#FUNÇÕES

#4 função com parâmetros de entrada, com retorno

def pode_lady_gaga(nome, ano_nasc, num_ingresso):
    #escopo local
    pode = False

    if 2025 - ano_nasc >= 16 and num_ingresso <= 250000:
        pode = True
        print(f'{nome} vai para o show de Lady Gaga')
    else:
        print(f'{nome} nao possui idade nem ingresso para o show de Lady Gaga')

    return pode

#escopo global

pode_lady_gaga(ano_nasc=1988, num_ingresso=888, nome='rene' )

pode_lady_gaga('rene', 1988, 90909 )